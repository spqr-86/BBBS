FROM python:3.9
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./project .
EXPOSE 8000
CMD gunicorn project.wsgi:application --bind 0.0.0.0:8000