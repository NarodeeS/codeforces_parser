from celery_conf import celery_app


@celery_app.task
def parse():
    pass
