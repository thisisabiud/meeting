from django.db import models

from .user_group import UserGroup

class Post(models.Model):
    user = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='post/%Y/%m/%d')
    title = models.CharField(max_length=50)
    body = models.TextField()
    is_verified = models.BooleanField(default=False)

