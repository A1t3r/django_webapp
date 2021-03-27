from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url('^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url('^proceed/', views.proceed_payment, name='proceed_payment'),
    url('^confirm/', views.confirm_payment, name='confirm_payment'),
]