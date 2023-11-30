from django.shortcuts import render
from .models import Product, Category


def categories(request):
    return {'categories': Category.objects.all()}


def all_products(request):
    products = Product.objects.all()
    return render(request, template_name='shop/home.html', context={'products': products})
