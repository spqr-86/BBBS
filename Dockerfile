FROM python:3.8.5

WORKDIR /code/project

COPY requirements_dev.txt /code

RUN pip3 install -r /code/requirements_dev.txt

COPY . /code

CMD gunicorn project.wsgi:application --bind 0.0.0.0:8000
