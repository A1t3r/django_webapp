from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),

    #path("", views.get_product_list, name="products in main page")
]