from flask import Flask
import pandas as pd 
from app.handlers.routes import configure_routes
from pathlib import Path


def test_local_data():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    parent_path = (Path(__file__).parent)
    file_path = (parent_path / "../../data/student-mat.csv").resolve()
    df = pd.read_csv(file_path, sep=";", index_col=False) 
    df = df.filter(['age', 'absences', 'health'])
    df = df.reset_index(drop=True)
    url = '/predict' 
    
    d = df.to_dict()

    for i in range(len(df)):
        age = pd.Series(d["age"].values())
        health = pd.Series(d["health"].values())
        absences = pd.Series(d["absences"].values())
        url = '/predict?' + "age=" + str(age[i]) + "&absences=" + str(absences[i]) + "&health=" + str(absences[i])
        response = client.get(url)
        assert response.status_code == 200
    assert response.status_code == 200

def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_predict_route_valid_input():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?age=18&absences=19&health=3'

    response = client.get(url)

    assert response.status_code == 200

def test_predict_route_invalid_input():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?age=18&absences=19'

    response = client.get(url)

    assert response.status_code == 500
