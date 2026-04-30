FROM python:3.9

WORKDIR /api

COPY . /api

RUN pip install mysql-connector-python fastapi uvicorn motor

EXPOSE 8000