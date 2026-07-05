import allure
from api.user_api import send_request

@allure.step("Создание заказа с авторизацией")
def create_order_auth(ingredients, token):
    """Создаёт заказ с переданным токеном (предполагается, что токен уже с префиксом 'Bearer')"""
    headers = {"Authorization": token}
    payload = {"ingredients": ingredients}
    return send_request("POST", "/orders", json=payload, headers=headers)

@allure.step("Создание заказа без авторизации")
def create_order_unauth(ingredients):
    """Создаёт заказ без заголовка Authorization"""
    payload = {"ingredients": ingredients}
    return send_request("POST", "/orders", json=payload)