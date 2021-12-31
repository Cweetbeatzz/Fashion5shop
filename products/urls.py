from django.urls.conf import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.products_view, name="products"),
    path("product/<slug:slug>/", views.products_details_view, name="products_detail"),
    path("product/{id}/", views.products_by_id_view, name="products_by_id"),
    path(
        "all_product_categories/",
        views.all_products_by_category_view,
        name="all_products_by_categories",
    ),
]
