from django.contrib.auth.forms import PasswordResetForm
from django.urls.conf import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .forms import (
    UserLoginForm,
    PwdResetForm,
    PwdResetConfirmForm,
)
from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/account/login"),
        name="logout",
    ),
    path(
        "activate/<slug:uidb64>/<slug:token>/", views.activate_account, name="activate"
    ),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile_edit/", views.edit_profile, name="profile_edit"),
    path("profile_delete/", views.delete_profile, name="profile_delete"),
    path(
        "profile/confirm_delete/",
        TemplateView.as_view(template_name="profile_delete_cofirmation.html"),
        name="delete_confirmation",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html", form_class=UserLoginForm
        ),
        name="login_view",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset_form.html",
            success_url="password_reset_comfirmation.html",
            email_template_name="password_reset_email.html",
            form_class=PwdResetForm,
        ),
        name="password_reset",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            # reset_url="password_reset_comfirmation.html",
            success_url="password_reset_complete.html",
            form_class=PwdResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
]
