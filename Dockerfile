FROM python:3.8.5

RUN mkdir /code

COPY requirements_dev.txt /code

RUN pip3 install -r /code/requirements_dev.txt

COPY . /code

WORKDIR /code/project

RUN python3 manage.py collectstatic --noinput

CMD gunicorn project.wsgi:application --bind 0.0.0.0:8000
