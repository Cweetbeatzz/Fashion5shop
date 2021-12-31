from django import forms
from django.db import models
from django.db.models import fields
from .models import UserBase
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)


class RegisterationForm(forms.ModelForm):
    #####################################################################################################################

    username = forms.CharField(
        label="Username", min_length=2, max_length=50, help_text="Required"
    )
    email = forms.EmailField(
        label="Email",
        max_length=100,
        help_text="Required",
        error_messages={"required": "Email is Required"},
    )
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    confirmpassword = forms.CharField(
        label="Confirm Password", max_length=100, widget=forms.PasswordInput
    )
    ##########################################################################
    class Meta:
        model = UserBase
        fields = (
            "username",
            "email",
        )

    ##########################################################################

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        r = UserBase.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already Exists")
        return username

    ##########################################################################

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd["password"] != cd["confirmpassword"]:
            raise forms.ValidationError("Passwords do not match")
        return cd["confirmpassword"]

    ##########################################################################

    def clean_email(self):
        email = self.cleaned_data["email"]
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already Exists")
        return email

    ##########################################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Username"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Email"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Password"}
        )
        self.fields["confirmpassword"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Confirm Password"}
        )

    ##########################################################################


#####################################################################################################################
class UserLoginForm(AuthenticationForm):
    pass


#####################################################################################################################


class UserEditForm:
    pass


#####################################################################################################################


class PwdResetForm(PasswordResetForm):
    def clean_email(self):
        cleaned_email = self.cleaned_data["email"]
        user_email = UserBase.objects.filter(email=cleaned_email)
        if not user_email:
            raise forms.ValidationError("Invalid Email")
        return cleaned_email


#####################################################################################################################


class PwdResetConfirmForm(SetPasswordForm):
    pass
