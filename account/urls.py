from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('account.views',
    url(r'^$', 'home', name='account-home'),
    url(r'^login/$', 'login', name='account-login'),
    url(r'^logout/$', 'logout', name='account-logout'),
    url(r'^register/$', 'register', name='account-register'),
    
    url(r'^address/add/$', 'add_address', name='account-address-add'),
    url(r'^address/(?P<address_id>\d+)/$', 'edit_address', name='account-address-edit'),
    url(r'^address/(?P<address_id>\d+)/delete/$', 'delete_address', name='account-address-delete'),
    url(r'^address/(?P<address_id>\d+)/setdefault/$', 'setdefault_address', name='account-address-setdefault'),
)