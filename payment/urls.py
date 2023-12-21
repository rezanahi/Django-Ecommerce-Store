from django.urls import path
from .views import BasketView, order_placed

app_name = 'payment'

urlpatterns = [
    path('', BasketView, name='basket'),
    path('orderplaced/', order_placed, name='order_placed'),


]

