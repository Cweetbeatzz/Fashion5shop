import cart
from products.models import Product
from decimal import Decimal

###########################################################
class Cart:
    pass

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("sessionkey")

        if "sessionkey" not in request.session:
            cart = self.session["sessionkey"] = {}
        self.cart = cart

    ###########################################################

    def add(self, product, quantity):
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {"price": str(product.price)}

        self.session.modified = True

    ###########################################################
    def __len__():
        """
        Gets the number of item requested from the cart list
        """

    ###########################################################

    def __iter__(self):
        """
        Collects the product id in the session data to query the database and return the products
        """
        product_id = self.cart.keys()
        products = Product.objects.filter(id__in=product_id)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]

    ###########################################################
    def grand_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    ###########################################################
    def delete(self, product):
        product_id = product

        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    ###########################################################

    def update(self, product, quantity):
        product_id = product

        if product_id not in self.cart:
            self.cart[product_id["quantity"]] = quantity
            self.session.modified = True
