#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"falk.maximilian@outlook.com"}

cd /app/

/opt/venv/bin/python manage.py migrate --noinput

# The || true is needed because otherwise the container would crash on startup if we run this and the user already exists
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true


