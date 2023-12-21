from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey', {})
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, product_qty):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'price': int(product.price), 'qty': product_qty}
        else:
            self.basket[product_id]['qty'] = product_qty
        self.session.modified = True

    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.session.modified = True

    def update(self, id, qty):
        product_id = str(id)
        if product_id in self.basket:
            self.basket[str(product_id)]['qty'] = qty
            self.session.modified = True


    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.product.filter(id__in=product_ids)
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    def sum(self):
        total = 0
        for item in self.basket.values():
            total += item['price'] * item['qty']
        return total

    def clear(self):
        # Remove basket from session
        del self.session['skey']
        self.session.modified = True