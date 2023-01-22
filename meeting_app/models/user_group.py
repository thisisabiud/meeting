from django.db import models

from .group import CustomGroup
from .user import CustomUser

class UserGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)
    is_member = models.BooleanField(default=True)
    is_groupAdmin = models.BooleanField(default=False)
