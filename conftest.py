import pytest
from api.client import StellarBurgersClient
from helpers import generate_user_data


@pytest.fixture
def client():
    return StellarBurgersClient()


@pytest.fixture
def created_user(client):
    user_data = generate_user_data()
    response = client.register(user_data)
    token = response.json().get("accessToken")
    yield user_data, token
    client.delete_user(token)


@pytest.fixture
def ingredient_ids(client):
    response = client.get_ingredients()
    data = response.json()
    ingredients = data.get("data", [])
    ids = [ing["_id"] for ing in ingredients[:2]]
    return ids