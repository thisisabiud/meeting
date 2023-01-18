from django.db import models

from .topic import Topic
from django.conf import settings

class Progress(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,
                                related_name='progress'
                                )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='progress'
                            )
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.topic} -> {self.user}"