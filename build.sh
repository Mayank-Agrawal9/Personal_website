#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py migrate


#For Creating SuperUser
#DJANGO_SUPERUSER_USERNAME=admin \
#DJANGO_SUPERUSER_PASSWORD=Mayank@16Splice \
#DJANGO_SUPERUSER_EMAIL="mayankagrawal6162@gmail.com" \
#python manage.py createsuperuser --noinput