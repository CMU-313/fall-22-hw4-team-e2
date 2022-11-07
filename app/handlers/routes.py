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
        # for each attribute, check that it is not None and that the value is valid

        absences = request.args.get('absences')
        if absences == None:
            return 'Bad request: must include absences value (integer between 0 and 93)', 500
        absences = int(absences)
        if (absences < 0 or absences > 93):
            return 'Bad request: value of absences must be between 0 and 93', 500
        
        # try both for capitalization        
        g1 = request.args.get('G1')
        if g1 == None:
            g1 = request.args.get('g1')
        if g1 == None:
            return 'Bad request: must include G1 value (integer between 0 and 20)', 500
        g1 = int(g1)
        if (g1 < 0 or g1 > 20):
            return 'Bad request: value of G1 must be between 0 and 20', 500

        g2 = request.args.get('G2')
        if g2 == None:
            g2 = request.args.get('g2')
        if g2 == None:
            return 'Bad request: must include G2 value (integer between 0 and 20)', 500
        g2 = int(g2)
        if (g2 < 0 or g2 > 20):
            return 'Bad request: value of G2 must be between 0 and 20', 500

        query_df = pd.DataFrame({
            'G1': pd.Series(g1),
            'G2': pd.Series(g2),
            'absences': pd.Series(absences)
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.ndarray.item(prediction))