from django.shortcuts import render
from .models import Product, Category


def all_products(request):
    product = Product.objects.all()
    return render(request, template_name='shop/home.html', context={'product': product})
