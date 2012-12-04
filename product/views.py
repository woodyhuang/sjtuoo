#coding: utf-8

from django import shortcuts
from django.template import RequestContext

from product.models import Product


def index(request):
    products = Product.objects.filter()
    
    category_id = request.GET.get('cid', '')
    if category_id:
        products = products.filter(category=category_id)
    
    return shortcuts.render_to_response('index.html',
                    {'products': products, 'category_id': category_id},
                    context_instance=RequestContext(request))


def detail(request, product_id):
    product = shortcuts.get_object_or_404(Product, id=product_id)
    
    return shortcuts.render_to_response('product/detail.html',
                    {'product': product, 'category_id': product.category.id},
                    context_instance=RequestContext(request))
    