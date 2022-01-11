from django.urls.conf import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.register_view, name="register"),
    path("", views.login_view, name="login"),
]
