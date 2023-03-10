from celery import Celery

from api.parse_tasks import parse_tasks


celery_app = Celery('celery_worker', broker='redis://redis:6379')


@celery_app.task
def parse():
    parse_tasks()


celery_app.conf.beat_schedule = {
    'parse-every-hour': {
        'task': 'celery_worker.parse',
        'schedule': 3600.0
    }
}
