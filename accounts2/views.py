from django.shortcuts import render

from accounts2.forms import CreateUserForm

# from .models import Register
from django.contrib.auth.forms import UserCreationForm

############################################

# Create your views here.
def register_view(request):
    form = CreateUserForm()

    if request.method == "post":
        form = CreateUserForm(request.post)
        if form.is_valid():
            form.save()

    return render(request, "register.html", {"form": form})


############################################


def login_view(request):
    return render(request, "login.html")


############################################


def update_users_view(request):
    pass


############################################


def delete_users_view(request):
    pass
