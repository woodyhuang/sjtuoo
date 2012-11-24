#coding: utf-8

from django import shortcuts
from django.template import RequestContext

from product.models import ProductCategory


def list_category(request):
    product_categories = ProductCategory.objects.all()
    
    return shortcuts.render_to_response('product/category_list.html',
                            {'product_categories': product_categories},
                            context_instance=RequestContext(request))
