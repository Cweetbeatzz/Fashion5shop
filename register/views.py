from django.shortcuts import render
from .models import Register

############################################

# Create your views here.
def register_view(request):
    return render(request, "register.html")


############################################


def register_users(_users):
    users = Register()
    _users = users.firstname
    pass


############################################


def update_users():
    pass


############################################
def delete_users():
    pass
