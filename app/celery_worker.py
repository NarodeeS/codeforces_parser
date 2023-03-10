from celery import Celery


celery_app = Celery('celery_worker', broker='redis://localhost:6379')


@celery_app.task
def parse():
    print('hello')


celery_app.conf.beat_schedule = {
    'parse-every-hour': {
        'task': 'celery_worker.parse',
        'schedule': 60.0
    }
}
