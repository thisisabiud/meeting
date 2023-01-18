from django.db import models

from .user import CustomUser

class UserProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M','Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Rather not say'
    user = models.OneToOneField(CustomUser, 
                                on_delete=models.CASCADE, 
                                related_name='profile'
                                )
    phone = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    date_of_birth = models.DateField(auto_now_add=True)
    gender = models.CharField(choices=Gender.choices, default=Gender.OTHER)
    location = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.user