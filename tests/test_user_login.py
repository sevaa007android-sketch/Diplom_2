import allure
from api.user_api import login_user

@allure.feature("Авторизация пользователя")
class TestUserLogin:

    @allure.title("Успешный вход существующего пользователя")
    def test_login_success(self, created_user):
        user_data, _ = created_user
        response = login_user({
            "email": user_data["email"],
            "password": user_data["password"]
        })
        assert response.status_code == 200
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Вход с неверным паролем")
    def test_login_wrong_password(self, created_user):
        user_data, _ = created_user
        response = login_user({
            "email": user_data["email"],
            "password": "wrong_password"
        })
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Вход с несуществующим email")
    def test_login_nonexistent_email(self):
        response = login_user({
            "email": "nonexistent@example.com",
            "password": "some_password"
        })
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Вход без пароля")
    def test_login_missing_password(self):
        response = login_user({
            "email": "some@example.com"
        })
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Вход без email")
    def test_login_missing_email(self):
        response = login_user({
            "password": "some_password"
        })
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"