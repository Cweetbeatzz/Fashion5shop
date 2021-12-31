from django.urls.conf import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_view, name="cart_view"),
    path("add/", views.cart_view_add, name="cart_view_add"),
    path("delete/", views.cart_view_delete, name="cart_view_delete"),
]
