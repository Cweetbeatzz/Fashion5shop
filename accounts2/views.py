from django.shortcuts import render
from .models import Register

############################################

# Create your views here.
def register_view(request):
    return render(request, "register.html")


############################################


def login_view(request):
    return render(request, "login.html")


############################################


def update_users_view(request):
    pass


############################################


def delete_users_view(request):
    pass
