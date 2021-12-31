from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from . import models

###############################################################

# Create your views here.
def products_home_view(request):
    return {"products_home_view": models.Product.objects.all()}


def products_view(request):
    products = models.Product.objects.all()
    return render(request, "products.html", {"products": products})


###############################################################
def products_details_view(request, slug):
    productsDetails = get_object_or_404(models.Product, slug=slug, in_stock=True)
    return render(request, "productDetails.html", {"productsDetails": productsDetails})


###############################################################


def products_by_id_view(request, id):
    productsIds = models.Product.objects.get(id=id)
    return render(request, "productDetails.html", {"productsIds": productsIds})


###############################################################


def products_by_category_view(request, category_slug):
    category = get_object_or_404(models.Category, slug=category_slug)
    productsCategory = models.Product.objects.filter(category=category)
    return render(
        request,
        "productbyCategories.html",
        {"category": category, "productsCategory": productsCategory},
    )


def all_products_by_category_view(request, category_slug):
    allcategory = get_object_or_404(models.Category, slug=category_slug)
    allproductsCategory = models.Product.objects.all(category=allcategory)
    return render(
        request,
        "categories.html",
        {"allcategory": allcategory, "allproductsCategory": allproductsCategory},
    )


###############################################################


def products_edit_view(request, id):
    search_product = models.Product.objects.filter(id)

    if search_product is None:
        return HttpResponseNotFound
    else:
        update_product = models.Product.objects.update(search_product)
    return render(request, "products.html", {"updateproduct": update_product})


###############################################################


def products_create_view(request, Product):
    products_create = models.Product.objects.create()
    return render(request, "products.html", {"productscreate": products_create})


###############################################################
def products_delete_view(id):
    search_product = models.Product.objects.filter(id)

    if search_product is None:
        return HttpResponseNotFound
    else:
        search_product = models.Product.objects.delete()


###############################################################
