from flask import Flask, jsonify, request
from flask_restx import Resource, Api
import joblib
import pandas as pd
import numpy as np
import os
app = Flask(__name__)
api = Api(app)

@app.route('/')
class Hello(Resource):
    def get(self):
        return "try the predict route it is great!"

@api.route('/predict', endpoint='predict')
@api.doc(params={'age': 'Age of applicant'})
@api.doc(params={'health': 'Health of applicant'})
@api.doc(params={'absences': 'Number of absences of applicant'})
class Predict(Resource):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    def get(self):
        #use entries from the query string here but could also use json
        age = request.args.get('age')
        absences = request.args.get('absences')
        health = request.args.get('health')
        data = [[age], [health], [absences]]
        query_df = pd.DataFrame({
            'age': pd.Series(age),
            'health': pd.Series(health),
            'absences': pd.Series(absences)
        })
        query = pd.get_dummies(query_df)
        prediction = self.clf.predict(query)
        print(prediction)
        return jsonify(np.ndarray.item(prediction))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
