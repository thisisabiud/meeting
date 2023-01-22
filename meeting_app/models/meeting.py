from django.db import models

from .group import CustomGroup

class Meeting(models.Model):
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE, related_name='meetings')
    held_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    address = models.CharField(max_length=50)
    key = models.CharField(max_length=8)
    is_online = models.BooleanField(default=False)
