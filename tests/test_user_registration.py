import allure
from api.user_api import register_user
from helpers import generate_user_data

@allure.feature("Регистрация пользователя")
class TestUserRegistration:

    @allure.title("Успешная регистрация нового пользователя")
    def test_register_user_success(self, created_user):
        user_data, token = created_user
        # Достаточно проверить, что токен получен (он есть, если регистрация успешна)
        assert token is not None, "Токен не получен"

    @allure.title("Регистрация уже существующего пользователя возвращает 403")
    def test_register_user_already_exists(self, created_user):
        user_data, _ = created_user
        response = register_user(user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Регистрация без email возвращает 403")
    def test_register_user_missing_email(self):
        user_data = generate_user_data()
        del user_data["email"]
        response = register_user(user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"