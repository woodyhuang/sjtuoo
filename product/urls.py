from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('product.views',
    url(r'^$', 'index', name='product-list'),
    url(r'^(?P<product_id>\d+)/$', 'detail', name='product-detail'),
)
