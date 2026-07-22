import allure
from helpers import generate_user_data


@allure.feature("Регистрация пользователя")
class TestUserRegistration:

    @allure.title("Успешная регистрация нового пользователя")
    def test_register_user_success(self, client):
        user_data = generate_user_data()
        response = client.register(user_data)
        token = response.json().get("accessToken")
        assert token is not None, "Токен не получен"
        client.delete_user(token)

    @allure.title("Регистрация уже существующего пользователя возвращает 403")
    def test_register_user_already_exists(self, client, created_user):
        user_data, _ = created_user
        response = client.register(user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Регистрация без email возвращает 403")
    def test_register_user_missing_email(self, client):
        user_data = generate_user_data()
        del user_data["email"]
        response = client.register(user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"