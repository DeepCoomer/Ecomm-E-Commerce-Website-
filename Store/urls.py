from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Store, name='store'),
    path('cart/', Cart, name='cart'),
    path('checkout/', Checkout, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order')
]
