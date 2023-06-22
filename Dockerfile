FROM python:latest

WORKDIR /project
COPY ./requirements .
COPY ./task .
RUN pip install -r requirements
RUN ./manage.py migrate
RUN ./manage.py loaddata fixtures.json


# 0.0.0.0: Этот вариант указывает серверу Django прослушивать все доступные сетевые интерфейсы
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
