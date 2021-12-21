from django.urls import path
from .views import *

urlpatterns = [
    path('', cart, name="cart"),
    path('remove_product/<int:product_id>/', remove_cart_item, name="cart_remove"),
    path('add_product/<int:product_id>/', add_cart, name="cart_add"),
    path('sub_product/<int:product_id>/', sub_cart, name="cart_sub")
]