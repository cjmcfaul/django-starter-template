import os
from .settings.base import env
from celery import Celery

app = Celery('{{ project_name }}')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))