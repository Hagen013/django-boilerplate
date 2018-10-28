from datetime import datetime, timedelta

import jwt

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from core.db.fields import PhoneNumberField
from core.db import TimeStamped
from .managers import UserManager

 
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        max_length=150,
        db_index=True,
        unique=True
    )

    email = models.EmailField(
        max_length=150,
        blank=True
    )

    first_name = models.CharField(
        max_length=150,
        blank=True
    )

    last_name = models.CharField(
        max_length=150,
        blank=True
    )

    patronymic = models.CharField(
        max_length=150,
        blank=True
    )

    phone_number = PhoneNumberField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    last_login = models.DateTimeField(
        default=timezone.now
    )
 
    objects = UserManager()
 
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
