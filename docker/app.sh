#!/bin/bash

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

gunicorn -b 0.0.0.0:8000 find_team.wsgi:application
