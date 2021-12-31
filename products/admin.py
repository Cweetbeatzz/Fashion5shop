from typing import List
from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "BusinessName", "category", "price"]
    list_filter = ["in_stock", "is_active"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
