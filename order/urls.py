from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('order.views',
    url(r'^(?P<order_id>\d+)/$', 'detail', name='order-detail'),
    url(r'^generate/$', 'generate', name='order-generate'),
    
    url(r'^item/add/$', 'add_item', name='order-item-add'),
    url(r'^item/(?P<product_id>\d+)/remove/$', 'remove_item', name='order-item-remove'),
)

urlpatterns += (
    url(r'^cart/$', 'django.views.generic.simple.direct_to_template', {'template': 'order/shop_cart.html'}, name="order-shop-cart"),
)
