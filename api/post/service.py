import os
import boto3
from botocore.exceptions import ClientError
from .models import Post

from api.user.models import CustomUserModel
from django.utils.timezone import now

s3 = boto3.client("s3")
BUCKET = os.getenv("AWS_STORAGE_BUCKET_NAME")
REGION = os.getenv("AWS_S3_REGION_NAME")
AWS_BASE_URL = (
    "https://"
    + os.getenv("AWS_STORAGE_BUCKET_NAME")
    + ".s3."
    + os.getenv("AWS_S3_REGION_NAME")
    + ".amazonaws.com/"
)


def upload_file_to_s3(file, post_id):
    key = "Posts/" + str(post_id) + "/" + file.name
    try:
        s3.upload_fileobj(file, BUCKET, key, ExtraArgs={"ACL": "public-read"})
    except ClientError as e:
        print(e)
    return AWS_BASE_URL + key


def addToUnread(newUnread, nowUser):
    try:
        post_obj = Post.objects.get(pk=newUnread["post"])
        postUser = post_obj.user
        newUnread["user"] = postUser
        newUnread["post"] = post_obj
    except:
        return None


