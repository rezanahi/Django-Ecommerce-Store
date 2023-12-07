from django.shortcuts import render, get_object_or_404
from .context_processors import Basket
from shop.models import Product
from django.http import JsonResponse


def basket_summary(request):
    basket = Basket(request)
    return render(request, template_name='basket/summary.html', context={'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product, product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'qty': basket_qty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product_id)
        basket_qty = basket.__len__()
        basket_total_price = basket.sum()
        response = JsonResponse({'qty': basket_qty, 'subtotal': basket_total_price})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product_id, product_qty)
        basket_qty = basket.__len__()
        basket_total_price = basket.sum()
        response = JsonResponse({'qty': basket_qty, 'subtotal': basket_total_price})
        return response