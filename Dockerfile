FROM python:3.8.5-alpine3.12 AS base
WORKDIR /app/

COPY poetry.lock pyproject.toml ./
RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev libffi-dev openssl-dev make && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root && \
    pip uninstall poetry -y && \
    apk del .build-deps
COPY . .