import allure
import requests
from data import BASE_URL


class StellarBurgersClient:

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    @allure.step("Отправить запрос {method} {endpoint}")
    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        return response

    @allure.step("Регистрация пользователя")
    def register(self, user_data):
        return self._send_request("POST", "/auth/register", json=user_data)

    @allure.step("Авторизация пользователя")
    def login(self, user_data):
        return self._send_request("POST", "/auth/login", json=user_data)

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self._send_request("DELETE", "/auth/user", headers=headers)

    @allure.step("Получение списка ингредиентов")
    def get_ingredients(self):
        return self._send_request("GET", "/ingredients")

    @allure.step("Создание заказа с авторизацией")
    def create_order_auth(self, ingredients, token):
        headers = {"Authorization": token}
        payload = {"ingredients": ingredients}
        return self._send_request("POST", "/orders", json=payload, headers=headers)

    @allure.step("Создание заказа без авторизации")
    def create_order_unauth(self, ingredients):
        payload = {"ingredients": ingredients}
        return self._send_request("POST", "/orders", json=payload)