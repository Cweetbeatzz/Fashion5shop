from django.urls.conf import path
from . import views


urlpatterns = [
    path("", views.contact_view, name="contact"),
]
