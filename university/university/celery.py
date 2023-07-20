from celery import Celery

app = Celery('tasks', broker="amqp://localhost", backend="redis://localhost")

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
