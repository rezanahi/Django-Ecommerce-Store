from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = basket.sum()
    return render(request, template_name='payment/home.html')
