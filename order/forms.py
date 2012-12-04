#coding: utf-8

from django.conf import settings


class ShoppingCardForm:
    """
    Not use classic Django form for less cache in session.
    Use this to display shopping card and store in session.
    item format: {
                    product_id: {
                        'name': product_name,
                        'count': count,
                        'price': price,
                    },
                }
    """
    def __init__(self, request):
#        del request.session[settings.SHOP_CART_KEY]
        cached = request.session.get(settings.SHOP_CART_KEY)
        if cached:
            self.products = cached['products']
            self.amount = cached['amount']
        else:
            self.products = {}
            self.amount = 0

    def remove_product(self, product_id):
        if self.products.has_key(product_id):
            del self.products[product_id]
    
    def set_product(self, product, count):
        self.products['%s' % product.id] = {'name': product.name,
                                     'count': count,
                                     'price': product.price,
                                     'thumbnail': str(product.image)}
        
    def update_price(self):
        self.amount = 0
        for p in self.products.itervalues():
            self.amount += p['price'] * p['count']
    
    def store(self, request):
        self.update_price()
        request.session[settings.SHOP_CART_KEY] = {'amount': self.amount,
                                                   'products': self.products}
    
    