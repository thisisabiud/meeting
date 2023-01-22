from django.db import models

from .topic import Topic

class CustomGroup(models.Model):
    name = models.CharField(max_length=40)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='group/%Y/%m/%d')
    progress = models.IntegerField(default=0)
    # token = 