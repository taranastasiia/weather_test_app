# Weather Query Web Application

Простое Django-приложение для запроса текущей погоды по названию города с использованием OpenWeatherMap API и сохранением истории запросов в PostgreSQL.

---

## Технологии

- Python 3.10+
- Django 5.2
- PostgreSQL
- OpenWeatherMap API
- Jinja-шаблоны (Django templates)
- Чистый CSS (без Bootstrap)

---

## Установка и запуск

1. Клонируйте репозиторий:
bash
git clone https://github.com/taranastasiia/weather-query-app.git
cd weather-query-app 

2. Создайте и активируйте виртуальное окружение
python -m venv venv
venv\Script\activate

3. Установите зависимости
pip install -r requirements.txt

4. Настройте базу данных PostgreSQL
Создайте базу данных:
CREATE DATABASE weather_db;
CREATE USER weather_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE weather_db TO weather_user;

5. Настройте переменные окружения
SECRET_KEY='your-django-secret-key'
OPENWEATHER_API_KEY='your_openweather_api_key'
NAME='weather_db'
USER='weather_user'
PASSWORD='yourpassword'
HOST='localhost'
PORT='5432'

Получить API-ключ можно на сайте: https://openweathermap.org/api

6. Примените миграции
python manage.py migrate

7. Запустите сервер разработки
python manage.py runserver

Приложение будет доступно по адресу: http://127.0.0.1:8000/



