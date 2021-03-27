from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.decorators.http import require_POST
from eshop.models import product
from eshop.views import index
from .cart import Cart


def cart_detail(request, pData={}, error=None):
    cart = Cart(request)
    col = []
    sum = 0
    for item in cart.storage.items():
        if (item[1] != 0):
            tmp_prod = get_object_or_404(product, id=item[0])
            col.append((item[0], tmp_prod.title, item[1]))
    return render(request, 'cart.html', {'cart': col, 'sum': cart.get_sum(), 'pData': pData, 'error': error})


def cart_add(request, product_id):
    cart = Cart(request)
    prod = get_object_or_404(product, id=product_id)
    if request.POST['quantity'] != "":
        try:
            cart.add_to_cart(prod=prod, N=int(request.POST['quantity']))
        except ValidationError:
            return index(request=request, error="Invalid value")
    else:
        try:
            cart.add_to_cart(prod=prod)
        except ValidationError:
            return index(request=request, error="Invalid value")
    return index(request)


#  return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    prod = get_object_or_404(product, id=product_id)
    if request.POST['quantity'] != "":
        try:
            cart.del_from_cart(prod=prod, N=int(request.POST['quantity']))
        except ValidationError:
            return cart_detail(request=request, error="Invalid value")
    else:
        try:
            cart.del_from_cart(prod=prod)
        except ValidationError:
            return cart_detail(request=request, error="Invalid value")
    return cart_detail(request)


def confirm_payment(request):
    cart = Cart(request)
    for item in cart.storage.items():
        prod = get_object_or_404(product, id=item[0])
        prod.in_stock -= item[1]
        prod.save()
    cart.erase_cart()
    pData={}
    pData['name'] = request.POST['name']
    pData['surname'] = request.POST['surname']
    pData['address'] = request.POST['address']
    return cart_detail(request, pData=pData)


def proceed_payment(request):
    template = loader.get_template('registration_form.html')
    return HttpResponse(template.render({}, request))
   # return confirm_payment(request)
