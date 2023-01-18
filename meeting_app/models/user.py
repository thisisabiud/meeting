from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        """
        create user with passed parameters
        """
        if not email:
            raise ValueError("Email must be provided")

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, first_name, last_name, email, password=None):
        """
        creating a superuser
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
            )

        user.is_admin = True
        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        return f'{self.email}'


    @property
    def get_fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    