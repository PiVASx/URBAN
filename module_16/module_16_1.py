from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Обработчик для главной страницы
@app.get('/', response_class=PlainTextResponse)
async def main() -> str:
    return "Главная страница"

# Обработчик для страницы администратора
@app.get('/user/admin', response_class=PlainTextResponse)
async def user_admin() -> str:
    return "Вы вошли как администратор"

# Обработчик для страницы пользователя по ID
@app.get('/user/{user_id}', response_class=PlainTextResponse)
async def user_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

# Обработчик для получения информации о пользователе
@app.get('/user', response_class=PlainTextResponse)
async def user(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
