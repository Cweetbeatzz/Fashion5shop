from django.urls.conf import path
from . import views
from products.views import products_by_category_view

app_name = "categories"

urlpatterns = [
    path("", views.categories_view, name="categories"),
    path(
        "category/<slug:category_slug>/",
        products_by_category_view,
        name="products_by_category",
    ),
]
