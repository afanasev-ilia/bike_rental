# bike_rental  

Сервис аренды велосипедов, написанный на Python с использованием Flask и SQLAlchemy.  
Позволяет пользователям арендовать велосипеды, а администраторам — управлять парком.

## 🛠️ Технологии  
- Python 3  
- Flask (веб-фреймворк)  
- SQLAlchemy (ORM)  
- PostgreSQL / SQLite (база данных)  
- Jinja2 (шаблонизация)  

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

4. Настройте базу данных в config.py.

5. Запустите приложение:

    ```bash
    flask run
    ```
