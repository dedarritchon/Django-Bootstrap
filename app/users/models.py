from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from django.db.models import Model, ForeignKey


class SystemUser(AbstractBaseUser, PermissionsMixin):

    class Meta:
        app_label = "users"

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    GROUP_ADMINS = 'Administrators'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
