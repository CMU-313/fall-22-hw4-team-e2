import os
from flask import Flask
import pandas as pd
from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_all_data():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "../../data/student-mat.csv")

    df = pd.read_csv(model_path, sep=";", index_col=False) 
    df = df.filter(['absences', 'G1', 'G2'])
    df = df.reset_index(drop=True)
    url = '/predict' 
    
    d = df.to_dict()

    for i in range(len(df)):
        g1 = pd.Series(d["G1"].values())
        g2 = pd.Series(d["G2"].values())
        absences = pd.Series(d["absences"].values())
        url = '/predict?' + "G1=" + str(g1[i]) + "&G2=" + str(g2[i]) + "&absences=" + str(absences[i])
        response = client.get(url)
        assert response.status_code == 200

def test_predict_route_valid_input():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?absences=18&G1=19&G2=3'

    response = client.get(url)

    assert response.status_code == 200

def test_predict_route_invalid_input():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?age=18&absences=19'

    response = client.get(url)

    assert response.status_code == 500

def test_predict_route_invalid_range():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?absences=18&G1=19&G2=21'
    response = client.get(url)
    assert response.status_code == 500

    url = '/predict?absences=100&G1=19&G2=18'
    response = client.get(url)
    assert response.status_code == 500

    url = '/predict?absences=0&G1=21&G2=18'
    response = client.get(url)
    assert response.status_code == 500
