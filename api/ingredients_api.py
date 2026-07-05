import allure
from api.user_api import send_request

@allure.step("Получение списка ингредиентов")
def get_ingredients():
    return send_request("GET", "/ingredients")