from django.shortcuts import render
from . import models

# Create your views here.
###############################################################


def categories_home_view(request):
    return {"categories_home_view": models.Category.objects.all().order_by("-id")}


###############################################################


def categories_view(request):
    categories = models.Category.objects.all().order_by("-id")
    return render(request, "categories.html", {"categories": categories})
