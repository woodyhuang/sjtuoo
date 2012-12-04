#coding: utf-8

from django import shortcuts
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import logout as do_logout, login as do_login, authenticate
from django.contrib.auth.views import login as login_view
from django.contrib.auth.decorators import login_required
from django.db import transaction

from account.models import ContactAddress
from account.forms import RegisterForm, LoginForm, ContactAddressForm
from order.forms import ShoppingCartForm


def register(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, u'恭喜你，注册成功。')
            do_login(request, authenticate(username=form.cleaned_data['email'],
                                           password=form.cleaned_data['password1']))
            return shortcuts.redirect(reverse('account-home'))
    else:
        form = RegisterForm()
    return shortcuts.render_to_response('account/register.html',
                                        {'form': form},
                                        context_instance=RequestContext(request))

def login(request):
    if request.user.is_authenticated():
        return shortcuts.redirect(reverse('account-home'))
    
    return login_view(request,
                      template_name='account/login.html',
                      authentication_form=LoginForm) # just show 'Email' as label for username

def logout(request):
    cart = ShoppingCartForm(request)
    
    do_logout(request)
    
    cart.store(request)
    return shortcuts.redirect(reverse('home'))


def home(request):
    return shortcuts.redirect(reverse('account-order-list'))


@login_required
def list_address(request):
    addresses = ContactAddress.objects.filter(user=request.user)
    
    return shortcuts.render_to_response('account/address_list.html',
                                        {'addresses': addresses},
                                        context_instance=RequestContext(request))

@login_required
@transaction.commit_on_success
def add_address(request):
    if request.POST:
        form = ContactAddressForm(request.POST)
        if form.is_valid():
            addr = form.save(request.user)
            
            if addr.is_default:
                setdefault_address(request, addr.id)
                
            messages.success(request, u'新的送货地址保存成功。')
            return shortcuts.redirect(reverse('account-address-list')) 
    else:
        form = ContactAddressForm()
        
    return shortcuts.render_to_response('account/address.html',
                                        {'form': form},
                                        context_instance=RequestContext(request))
    
@login_required
def edit_address(request, address_id):
    c = shortcuts.get_object_or_404(ContactAddress, id=address_id, user=request.user)
    if request.POST:
        form = ContactAddressForm(request.POST, instance=c)
        if form.is_valid():
            addr = form.save(request.user)
            if addr.is_default:
                setdefault_address(request, addr.id)
            messages.success(request, u'送货地址更改成功。')
            return shortcuts.redirect(reverse('account-address-list'))
    else:
        form = ContactAddressForm(instance=c)
    return shortcuts.render_to_response('account/address.html',
                                        {'form': form},
                                        context_instance=RequestContext(request))

@login_required
def delete_address(request, address_id):
    c = shortcuts.get_object_or_404(ContactAddress, id=address_id, user=request.user)
    c.delete()
    messages.success(request, u'送货地址成功删除。')
    return shortcuts.redirect(reverse('account-address-list'))


@login_required
@transaction.commit_on_success
def setdefault_address(request, address_id):
    c = shortcuts.get_object_or_404(ContactAddress, id=address_id, user=request.user)
    
    ContactAddress.objects.filter(user=request.user, is_default=True).update(is_default=False)
    
    c.is_default = True
    c.save()
    messages.success(request, u'默认的送货地址更改成功。')
    return shortcuts.redirect(reverse('account-address-list'))
