from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def categories(request):
    return {'categories': Category.objects.all()}


def all_products(request):
    products = Product.objects.all()
    return render(request, template_name='shop/home.html', context={'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, template_name='product/detail.html', context={'product': product})


def category_list(request, slug_category):
    category = get_object_or_404(Category, slug=slug_category)
    products = Product.objects.filter(category=category)
    return render(request,
                  template_name='product/category_list.html',
                  context={'category': category, 'products': products})
