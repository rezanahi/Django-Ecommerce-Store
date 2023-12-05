from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('book/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:slug_category>/', views.category_list, name='category_list')
]