from django.test import TestCase, Client
from shop.models import Category, Product
from django.contrib.auth.models import User
from django.urls import reverse
from shop.views import all_products
from django.http import HttpRequest

class TestViewResponse(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django 4', created_by_id=1, slug='django_4', price=20
                                            , image='django')

    def test_url_allowed_host(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse(viewname='shop:product_detail', args=['django_4']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse(viewname='shop:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        response = all_products(HttpRequest())
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))