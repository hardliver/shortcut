#!/bin/sh

python manage.py makemigrations --noinput
python manage.py migrate

if [ -n "$SUPERUSER" ] && [ -n "$SUPERUSERPASSWORD" ]
then
    echo "
from django.contrib.auth.models import User;
if not User.objects.filter(username='$SUPERUSER').exists():
    User.objects.create_superuser('$SUPERUSER', '', '$SUPERUSERPASSWORD')
    " | python manage.py shell
fi

python manage.py runserver 0.0.0.0:8000
