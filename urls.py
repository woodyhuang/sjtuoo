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
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}, name='home'),
    
    url(r'^account/', include('account.urls')),
    
    url(r'^product/category/$', 'product.views.list_category', name='product-list-category'),
)
