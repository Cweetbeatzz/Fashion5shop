from django.db import models

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    postalcode = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    confirmpassword = models.CharField(max_length=100, null=False)
    createdat = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self
