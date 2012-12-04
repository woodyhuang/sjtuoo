#coding: utf-8

from django import shortcuts
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import transaction

from account.models import ContactAddress
from product.models import Product
from order.models import Order, OrderItem
from order.forms import ShoppingCartForm


@login_required
def my_order(request):
    return shortcuts.render_to_response('order/list.html',
                    {'orders': Order.objects.all()},
                    context_instance=RequestContext(request))
    

@login_required
def generate(request):
    if request.POST:
        cart = ShoppingCartForm(request)
        address_id = request.POST.get('address', '')
        if not address_id:
            messages.error(request, u'请选择一个送货地址。')
            return shortcuts.redirect(reverse('order-generate'))
        address = shortcuts.get_object_or_404(ContactAddress, id=address_id, user=request.user)
        
        with transaction.commit_on_success():
            order = Order(owner=request.user,
                          address=str(address),
                          description=request.POST.get('description', ''),
                          amount=cart.amount)
            order.save()
            
            for pid, p in cart.products.iteritems():
                OrderItem(order=order,
                           product=shortcuts.get_object_or_404(Product, id=pid),
                           price=p['price'],
                           count=p['count']
                           ).save()
                           
            cart.delete(request)
            messages.success(request, u'下单成功！请等待系统确认。')
            return shortcuts.redirect(reverse('order-detail', args=[order.id]))
    
    addresses = ContactAddress.objects.filter(user=request.user)
    if not addresses:
        messages.error(request, u'你还没有送货地址，请创建至少一个送货地址。')
        return shortcuts.redirect(reverse('account-address-add'))
    
    return shortcuts.render_to_response('order/generate.html',
                    {'addresses': addresses},
                    context_instance=RequestContext(request))


def detail(request, order_id):
    order = shortcuts.get_object_or_404(Order, id=order_id)
    return shortcuts.render_to_response('order/detail.html',
                    {'order': order},
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
    
    cart = ShoppingCartForm(request)
    cart.set_product(product, count)
    cart.store(request)
    
    return shortcuts.render_to_response('order/shop_cart.html',
                    context_instance=RequestContext(request))


def remove_item(request, product_id):
    cart = ShoppingCartForm(request)
    cart.remove_product(product_id)
    cart.store(request)
    
    return shortcuts.render_to_response('order/shop_cart.html',
                    context_instance=RequestContext(request))
    