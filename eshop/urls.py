from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:product_id>/", views.product_details, name="detailed product info"),
    path("about/", views.about, name="about"),
]
