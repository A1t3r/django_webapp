from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from eshop.models import product
from cart.cart import Cart


def index(request, error=None):
    cart = Cart(request)
    prodc = product.objects.order_by('title')
    template = loader.get_template('eshop/index.html')
    context = {
        'products': prodc,
        'c': cart.get_sum(),
        'q': cart.get_q(),
        'error': error,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('eshop/about.html')
    return HttpResponse(template.render({}, request))


def product_details(request, product_id):
    prodc = product.objects.get(id=product_id)
    template = loader.get_template('eshop/product.html')
    context = {
        'product': prodc,
    }
    return HttpResponse(template.render(context, request))
