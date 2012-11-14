from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('account.views',
    url(r'^$', 'home', name='account-home'),
    url(r'^login/$', 'login', name='account-login'),
    url(r'^logout/$', 'logout', name='account-logout'),
    url(r'^register/$', 'register', name='account-register'),
)