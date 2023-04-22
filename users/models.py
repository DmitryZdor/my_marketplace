from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', auto_now=False, null=True, blank=True)


