from django.db import models
from django.db.models.deletion import CASCADE
from ..user.models import CustomUserModel
import os



# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return f"{self.post_title} ({self.post_id})"

    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUserModel, related_name="post", on_delete=CASCADE)

    # will be post_city, post_state
    post_title = models.CharField(null=False, max_length=100)
    post_content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class SavedPost(models.Model):
    saved_post_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    user = models.ForeignKey(
        CustomUserModel, related_name="saved_post", on_delete=CASCADE
    )


