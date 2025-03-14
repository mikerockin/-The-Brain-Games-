FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

LABEL authors="mikhail"

RUN apk update && apk add make

ENV POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    VIRTUAL_ENV="/venv"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir poetry==1.8.3

RUN make install






