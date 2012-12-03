#coding: utf-8

from django import shortcuts
from django.template import RequestContext

from product.models import ProductCategory


def index(request):
    products = []
    
    return shortcuts.render_to_response('index.html',
                            {'products': products},
                            context_instance=RequestContext(request))
