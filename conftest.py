import pytest
from helpers import generate_user_data
from api.user_api import register_user, delete_user
from api.ingredients_api import get_ingredients

@pytest.fixture
def new_user_data():
    return generate_user_data()

@pytest.fixture
def created_user(new_user_data):
    user_data = new_user_data
    response = register_user(user_data)
    token = response.json()["accessToken"]
    yield user_data, token
    delete_user(token)

@pytest.fixture
def ingredient_ids():
    response = get_ingredients()
    data = response.json()
    # Берём первые два ID из списка ингредиентов
    ingredients = data.get("data", [])
    ids = [ing["_id"] for ing in ingredients[:2]]
    return ids