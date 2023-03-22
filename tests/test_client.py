import pytest
from delivery_cost_calculator import create_app

@pytest.fixture()
def app():
    app = create_app()
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_request(client):
    response = client.post('/', json = {
        "cart_value": 1000,
        "delivery_distance": 0, 
        "number_of_items": 0,
        "time": "2021-10-12T17:00:00Z",
        })

    assert response.data == b'{"delivery_fee": 200}'

def test_post_request_without_json(client):
    response = client.post('/', data="")
    assert response.data == b'400 Bad Request: The request did not contain JSON.\n'

