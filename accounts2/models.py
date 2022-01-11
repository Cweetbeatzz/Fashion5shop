from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False, unique=True)
    email = models.EmailField(max_length=100, null=False, unique=True)
    phone = models.CharField(max_length=15, null=False)
    state = models.CharField(max_length=100, null=False)
    country = CountryField()
    address_line_1 = models.CharField(max_length=150, blank=True)
    address_line_2 = models.CharField(max_length=150, blank=True)
    postalcode = models.CharField(max_length=12, null=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self


class Login(models.Model):
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
