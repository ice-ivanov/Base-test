import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')

app = Celery('drf')
app.config_from_object('django.conf:settings', namespace='CELERY', force=True)
app.autodiscover_tasks()

print('LOOK HERE')
print(app.conf)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
