import allure


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth(self, client, created_user, ingredient_ids):
        _, token = created_user
        response = client.create_order_auth(ingredient_ids, token)
        assert response.status_code == 200
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, client, ingredient_ids):
        response = client.create_order_unauth(ingredient_ids)
        assert response.status_code == 200
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без ингредиентов возвращает 400")
    def test_create_order_no_ingredients(self, client, created_user):
        _, token = created_user
        response = client.create_order_auth([], token)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидным хешем ингредиента возвращает 500")
    def test_create_order_invalid_ingredient(self, client, created_user):
        _, token = created_user
        response = client.create_order_auth([1, 1323], token)
        assert response.status_code == 500