from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

from categories.models import Category


# Create your models here.
############################################################################################


class Product(models.Model):
    name = models.CharField(null=False, max_length=70)
    image = models.ImageField(null=False, upload_to="images/")
    BusinessName = models.CharField(null=False, max_length=70, default="null")
    description = models.TextField(null=False, max_length=200)
    category = models.ForeignKey(
        Category, related_name="product", null=False, on_delete=models.CASCADE
    )
    price = models.DecimalField(
        null=False, max_digits=10, decimal_places=2, default=0.0
    )
    Date_added = DateTimeField(auto_now_add=True)
    Date_updated = DateTimeField(auto_now=True)
    Created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product_creator",
    )
    slug = models.SlugField(max_length=100)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    #############################################

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-Date_added",)

    #############################################

    def get_absolute_url(self):
        return reverse("products:products_detail", args=[self.slug])

    #############################################

    def __str__(self):
        return self.name
