from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .cart import Cart
from products.models import Product
import json

# Create your views here.
def cart_view(request):
    return render(request, "cart.html")


def cart_view_add(request):
    cart_session = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product = get_object_or_404(Product, id=product_id)
        cart_session.add(product=product)
        response = JsonResponse({"product": product.name})
        return response


def cart_view_update(request):
    data = json.loads(request.data)
    productId = data["productid"]
    action = data["action"]
    response = JsonResponse({"test": "data"}, safe=False)
    return response


def cart_view_delete(request):
    cart_session = Cart(request)
    if request.POST.get("action") == "delete":
        product_id = int(request.POST.get("productid"))
        cart_session.delete(product=product_id)
