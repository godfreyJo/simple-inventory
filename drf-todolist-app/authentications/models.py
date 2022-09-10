from django.db import models
from helpers.models import TrackingModel
from django.Contrib.auth.models import (PermissionMixin, BaseUserManager, AbstractBaseUser)

# Create your models here.


class User(AbstractBaseUser, BaseUserManager, PermissionMixin, TrackingModel):
    pass