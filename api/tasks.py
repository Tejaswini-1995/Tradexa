from celery import shared_task
import os


@shared_task
def upload_file(model, foreign_key, ):
    bucket = os.getenv('S3_BUCKET', 'tradexa')
