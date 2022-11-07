import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        absences = request.args.get('absences')
        g1 = request.args.get('G1')
        g2 = request.args.get('G2')
        query_df = pd.DataFrame({
            'G1': pd.Series(g1),
            'G2': pd.Series(g2),
            'absences': pd.Series(absences)
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.ndarray.item(prediction))