# bike_rental  

Django-приложение для аренды велосипедов с базовой функциональностью бронирования, управления парком и пользователями

## 🛠️ Технологии  
Python 3.10
Django 4.2

## 🚀 Установка  
1. Клонируйте репозиторий:  
   ```bash
   git clone https://github.com/afanasev-ilia/bike_rental.git
   cd bike_rental
   ```

2. Создайте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate    # Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Настройте базу данных:
    Отредактируйте DATABASES в settings.py (по умолчанию SQLite).

    Для PostgreSQL укажите свои параметры:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bike_rental',
            'USER': 'your_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
5. Примените миграции:
    ```bash
    python manage.py migrate
    ```
6. Создайте суперпользователя (для доступа в админку):
    ```bash
    python manage.py createsuperuser
    ```
7. Запустите сервер:
    ```bash
    python manage.py runserver
    ```
    
Откройте в браузере:

Основное приложение: http://127.0.0.1:8000

Админ-панель: http://127.0.0.1:8000/admin
