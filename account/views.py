from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from account.models import UserBase
from .forms import RegisterationForm, UserEditForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

# Create your views here.

##########################################################################
@login_required
def dashboard(request):
    return render(request, "dashboard.html", {"section": "profile", "orders": "orders"})
    ##########################################################################


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        register_form = RegisterationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.email = register_form.cleaned_data["email"]
            user.set_password(register_form.cleaned_data["password"])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Activate your account"
            message = render_to_string(
                "account_activate_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            user.email_user(subject=subject, message=message)
            return HttpResponse(
                "Registered! Successfully sent activation to your Email"
            )
    else:
        register_form = RegisterationForm()
        return render(
            request,
            "account_activate_email.html",
            {"form": register_form},
        )

    ##########################################################################


def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except:
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("account:dashboard")
    else:
        return render(request, "account_activate_invalid.html")

    ##########################################################################


@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, "profile_edit.html", {"user_form": user_form})

    ##########################################################################


@login_required
def delete_profile(request):
    user = UserBase.objects.get(username=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect("account:delete_confirmation")
