from django.urls import path
from .views import BasketView

app_name = 'payment'

urlpatterns = [
    path('', BasketView, name='basket'),

]

