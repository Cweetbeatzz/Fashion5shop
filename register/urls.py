from django.urls.conf import path
from . import views


urlpatterns = [
    path("", views.register_view, name="register"),
]
