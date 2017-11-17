#!/bin/bash
echo 'Migrating ...'
python manage.py migrate

echo 'Running loaddata ...'
python manage.py loaddata free_templates --verbosity=3
python manage.py loaddata free_charts --verbosity=3

echo 'Creating superuser admin/admin'
echo "from django.contrib.auth.models import User; user = User.objects.create_superuser('admin', 'admin@example.com', 'admin'); user.first_name = 'Admin'; user.save();" | python manage.py shell

echo 'Collecting static ...'
python manage.py collectstatic --noinput

echo 'Starting Gunicorn ...'
gunicorn chart_admin.wsgi -b 0.0.0.0:8000

echo 'Done!'