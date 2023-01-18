from django.db import models


class Topic(models.Model):

    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = '-name'