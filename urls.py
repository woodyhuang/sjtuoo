from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django import template
template.add_to_builtins('common.mytags')


urlpatterns = patterns('',
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     
    # home 
    url(r'^$', 'product.views.index', name='home'),
    
    url(r'^account/', include('account.urls')),
    url(r'^product/', include('product.urls')),
)
