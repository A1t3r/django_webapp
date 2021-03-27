from django.conf import settings
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from eshop.models import product


class Cart:
    storage = {}
    cart_sum = 0
    q = 0

    def __init__(self, request):
        #  prodc = product.objects.all()
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def get_q(self):
      #  q = 0
      #  for item in self.storage.values():
       #     q += item
        return Cart.q

    def get_sum(self):
     #   sum = 0
     #   for item in self.storage.items():
     #       sum += get_object_or_404(product, id=item[0]).cost * item[1]
        return Cart.cart_sum

    def erase_cart(self):
        Cart.cart_sum = 0
        Cart.q = 0
        self.storage.clear()

    def save_cart(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add_to_cart(self, prod, N=1):
        if prod.id in self.storage:
            if 0 > N or N + self.storage[prod.id] > prod.in_stock:
                raise ValidationError('Invalid value', code='invalid')
        else:
            if 0 > N or N > prod.in_stock:
                raise ValidationError('Invalid value', code='invalid')

        if prod.id in self.storage:
            self.storage[prod.id] += N
        else:
            self.storage[prod.id] = N
        Cart.cart_sum += prod.cost * N  #
        Cart.q += N
        self.save_cart()

    def del_from_cart(self, prod, N=1):
        if 0 > N or N > self.storage[prod.id]:
            raise ValidationError('Invalid value', code='invalid')
        self.storage[prod.id] -= N
        Cart.cart_sum -= prod.cost * N #
        Cart.q -= N
        self.save_cart()
