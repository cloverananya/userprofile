from django.utils.translation import gettext as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
        GENDER = (
            ('Male', 'Boy'),
            ('Female', 'Girl'),
        )
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
        gender = models.CharField(max_length=10, choices=GENDER)
        number = models.PositiveIntegerField()
        fav_actor = models.CharField(max_length=250)
        date_of_birth = models.DateField()
        image = models.ImageField(blank=True, null=True)


