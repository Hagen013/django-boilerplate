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

 
class User(AbstractBaseUser, PermissionsMixin, TimeStamped):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    """

    email = models.EmailField(
        max_length=64,
        db_index=True,
        unique=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=30,
        blank=True
    )

    last_name = models.CharField(
        max_length=30,
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

    last_login = models.DateTimeField(
        default=timezone.now
    )
 
    objects = UserManager()
 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        payload = {
            "id": self.pk,
            "exp": int(dt.strftime('%s'))
        }
        token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm="HS256"
        )
        return token.decode("utf-8")

    def __str__(self):
        return self.email
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

