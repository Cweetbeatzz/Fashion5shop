from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

    # def __str__(self):
    #     return self
