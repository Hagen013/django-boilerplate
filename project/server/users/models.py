from django.db import models
from django.utils import timezone
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
    # USER_TYPE_CHOICES = (
    #     (1, 'client'),
    #     (2, 'manager'),
    #     (3, 'operator'),
    #     (4, 'admin'),
    # )

    # user_type = models.PositiveSmallIntegerField(
    #     choices=USER_TYPE_CHOICES
    # )

    email = models.EmailField(
        max_length=64,
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
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
