from django.db import models

from .group import CustomGroup

class Notification(models.Model):
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    body = models.TextField()