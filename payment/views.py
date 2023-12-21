import json


from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from basket.basket import Basket
from order.views import payment_confirmation


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.sum())
    total = total.replace('.', '')
    total = int(total)

    # stripe.api_key = ''
    # intent = stripe.PaymentIntent.create(
    #     amount=total,
    #     currency='gbp',
    #     metadata={'userid': request.user.id}
    # )

    return render(request, 'payment/home.html',
                  {'client_secret': UniqueNumberGenerator.get_unique_number()})


class UniqueNumberGenerator:
    current_number = -1  # Start from -1 so the first call returns 0

    @classmethod
    def get_unique_number(self):
        self.current_number += 1
        return self.current_number