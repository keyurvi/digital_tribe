from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    CLIENT = 1
    MANAGER = 2

    ROLE_CHOICES = (
        (CLIENT, 'Client'),
        (MANAGER, 'Manager'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False)