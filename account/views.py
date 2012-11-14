#coding: utf-8

from django import shortcuts
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import logout as do_logout, login as do_login, authenticate
from django.contrib.auth.views import login as login_view
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

#from account.forms import RegisterForm, ContactForm, UserProfileChangeForm
from account.models import ContactAddress
from account.forms import RegisterForm, LoginForm


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


@login_required
def logout(request):
    do_logout(request)
    return shortcuts.redirect(reverse('home'))


@login_required
def home(request):
    addresses = ContactAddress.objects.filter(user=request.user)
    
    return shortcuts.render_to_response('account/home.html',
                                        {'addresses': addresses},
                                        context_instance=RequestContext(request))
    