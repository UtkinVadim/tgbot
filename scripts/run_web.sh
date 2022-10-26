#!/bin/sh

cd /app
python manage.py migrate
python manage.py createcachetable
python manage.py collectstatic --no-input
uwsgi --ini uwsgi.ini
