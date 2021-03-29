import os
from celery import Celery, shared_task

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('drf')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task
def hello():
    print('Hello there!')
