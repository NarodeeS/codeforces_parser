from celery import Celery

from service.parse_tasks import parse_tasks
from service.allocate_contests import allocate_contests


celery_app = Celery('celery_worker', broker='redis://redis:6379')


@celery_app.task
def parse():
    parse_tasks()
    allocate_contests()


celery_app.conf.beat_schedule = {
    'parse-every-hour': {
        'task': 'celery_worker.parse',
        'schedule': 3600.0
    }
}
