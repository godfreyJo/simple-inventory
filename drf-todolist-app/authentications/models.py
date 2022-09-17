from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (PermissionsMixin, BaseUserManager, AbstractBaseUser)

# Create your models here.

class UserManager(BaseUserManager):


    def create_user(self, username, email,password=None):

        if username is None:
            raise TypeError('user should have a username')
        if email is None:
            raise TypeError('user should have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        if password is None:
            raise TypeError('user should have a password')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

        


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField( max_length=250,unique=True, db_index=True)
    email = models.EmailField( max_length=250,unique=True, db_index=True)
    is_verified=models.BooleanField( default=False)
    is_active=models.BooleanField( default=True)
    is_staff=models.BooleanField( default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''
    
    # is_staff = models.BooleanField(
    #     _('staff status'),
    #     default=False,
    #     help_text=_(
    #         'Designates whether the user can log into this admin site.'),
    # )
    # is_active = models.BooleanField(
    #     _('active'),
    #     default=True,
    #     help_text=_(
    #         'Designates whether this user should be treated as active. '
    #         'Unselect this instead of deleting accounts.'
    #     ),
    # )
    # date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    # email_verified = models.BooleanField(
    #     _('email_verified'),
    #     default=False,
    #     help_text=_(
    #         'Designates whether this users email is verified. '

    #     ),
    # )
    

    
