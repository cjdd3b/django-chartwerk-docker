from __future__ import absolute_import
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chart_admin.settings')

app = Celery('chartwerk')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
  task_serializer='json'
)
# Use synchronous tasks in local dev 
if settings.DEBUG:
  app.conf.update(task_always_eager=True)

# If debug isn't on, celery doesn't seem to connect (and loaddata doesn't work) Why?
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name='celery')