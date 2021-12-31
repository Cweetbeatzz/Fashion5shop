from django.urls.conf import path
from . import views


urlpatterns = [
    path("", views.about_view, name="about"),
]
