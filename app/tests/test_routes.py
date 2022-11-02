from flask import Flask

from app.handlers.routes import configure_routes


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
