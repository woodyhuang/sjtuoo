#coding: utf-8

from django import shortcuts
from django.template import RequestContext
from django.contrib import messages

from product.models import Product
from order.forms import ShoppingCardForm


def index(request):
    products = Product.objects.filter()
    
    category_id = request.GET.get('cid', '')
    if category_id:
        products = products.filter(category=category_id)
    
    return shortcuts.render_to_response('index.html',
                    {'products': products, 'category_id': category_id},
                    context_instance=RequestContext(request))


def add_item(request):
    product_id = request.REQUEST.get('pid', '')
    try:
        count = int(request.REQUEST.get('count', '1'))
        if count < 1:
            raise
    except:
        messages.error(request, u'您输入的商品数量错误，请重新输入。')
        return shortcuts.render_to_response('order/shop_cart.html',
                    context_instance=RequestContext(request))
    
    product = shortcuts.get_object_or_404(Product, id=product_id)
    
    cart = ShoppingCardForm(request)
    cart.set_product(product, count)
    cart.store(request)
    
    return shortcuts.render_to_response('order/shop_cart.html',
                    context_instance=RequestContext(request))


def remove_item(request, product_id):
    cart = ShoppingCardForm(request)
    cart.remove_product(product_id)
    cart.store(request)
    
    return shortcuts.render_to_response('order/shop_cart.html',
                    context_instance=RequestContext(request))
    