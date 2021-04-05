from ..drf.celery_app import app


@app.task(name='hello')
def hello():
    print('Hello')
