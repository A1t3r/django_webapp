from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.decorators.http import require_POST
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


def get_product(request, product_id):
    prodc = product.objects.get(id=product_id)
    template = loader.get_template('product.html')
    context = {
        'title': prodc.title,
        'description': prodc.description,
        'cost': prodc.cost,
        'in_stock': prodc.in_stock
    }
    return HttpResponse(template.render(context, request))
