from django.db import models
from django.urls.base import reverse

# Create your models here.
############################################################################################
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def categories_absolute_url(self):
        return reverse("categories:products_by_category", args=[self.slug])

    def __str__(self):
        return self.name
