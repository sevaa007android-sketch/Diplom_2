import time

def generate_user_data():
    timestamp = int(time.time() * 1000)
    return {
        "email": f"test_{timestamp}@yandex.ru",
        "password": "password123",
        "name": f"User_{timestamp}"
    }