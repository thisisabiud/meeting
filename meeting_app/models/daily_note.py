from django.db import models

from .progress import Progress

class Note(models.Model):
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='notes/%Y/%m/%d', blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.progress