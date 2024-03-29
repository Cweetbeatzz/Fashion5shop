from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db.models import fields

from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("SuperUser must be assigned is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("SuperUser must be assigned is_superuser=True.")

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


# Create your models here.
class UserBase(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False, unique=True)
    email = models.EmailField(_("email address"), null=False, unique=True)
    phone = models.CharField(max_length=15, null=False)
    state = models.CharField(max_length=100, null=False)
    # delivery details
    country = CountryField()
    address_line_1 = models.CharField(max_length=150, blank=True)
    address_line_2 = models.CharField(max_length=150, blank=True)
    postalcode = models.CharField(max_length=12, null=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    block_user_account = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.username
