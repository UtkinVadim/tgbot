FROM python:3.10.2-alpine
WORKDIR /app

RUN apk update
RUN apk add --virtual .build-deps \
    gcc python3-dev musl-dev postgresql-dev \
    linux-headers libffi-dev jpeg-dev zlib-dev  # for Pillow and psycopg2

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apk add --update busybox-suid

RUN addgroup -S tgbot
RUN adduser -S -H -G tgbot tgbot

RUN chown -R tgbot:tgbot /app

USER tgbot
