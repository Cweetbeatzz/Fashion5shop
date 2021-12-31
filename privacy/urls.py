from django.urls.conf import path
from . import views


urlpatterns = [
    path("", views.privacy_view, name="privacy"),
]
