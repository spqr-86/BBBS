# BBBS
### Описание
Сайт предназначен для помощи наставникам в работе с детьми.
### Технологии
- Python 3.8.5
- Django 3.0.5
- Django Rest Framework 3.11.0
- gunicorn 20.0.4
- Docker 20.10.6
- docker-compose 1.25.0
- Nginx 1.19.3
- Postgres 12.4
### Начало работы
Для начала клонируем репозиторий в нужный каталог, после этого создаём виртуальное окружение одним из способов:

1.

```python3 -m venv venv```  

И активируем виртуальное окружение:  

```source venv/bin/activate``` для Linux и  

```source venv/Scripts/activate``` для Windows.  

Чтобы установить все зависимости, из корня проекта выполняем:

```pip3 install -r requirements.txt``` для прода


```pip3 install -r requirements_dev.txt``` для разработки

2.

```pip install pipenv```

Активируем виртуальное окружение:

```pipenv shell```

Чтобы установить все зависимости, из корня проекта выполняем:

```pipenv install``` для прода


```pipenv install --dev``` для разработки


### Настройки проекта

В папке ./project/project находятся файлы с настройками: settings.py и settings_dev.py

Для хранения переменных используется файл .env, его нужно создать самостоятельно по примеру example.env

Переменная DJANGO_DEVELOPMENT определяет будет ли использован файл с настройками для разработки: settings_dev.py
