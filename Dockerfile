FROM python:3.11-alpine3.18

COPY requirements.txt /app/requirements.txt
COPY mydjango /app/mydjango
COPY myscrapy /app/myscrapy
WORKDIR /app

RUN apk add postgresql-client build-base postgresql-dev

RUN apk add libffi libffi-dev

RUN pip install -r /app/requirements.txt

RUN adduser --disabled-password app-user

USER app-user