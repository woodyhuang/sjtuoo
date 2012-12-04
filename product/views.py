#coding: utf-8

from django import shortcuts
from django.template import RequestContext

from product.models import Product


def list_product(request):
    product = Product.objects.all()
    
    return shortcuts.render_to_response('product/product_list.html',
                            {'product': product},
                            context_instance=RequestContext(request))
