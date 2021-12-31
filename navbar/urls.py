from django.urls.conf import path
from . import views


urlpatterns = [
    path("", views.navbar_view, name="navbar"),
]
