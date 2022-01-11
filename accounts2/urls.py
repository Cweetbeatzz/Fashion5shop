from django.urls.conf import path
from . import views


app_name = "accounts2"

urlpatterns = [
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
]
