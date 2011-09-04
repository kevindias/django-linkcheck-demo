from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('linkshare.views',
    url(r'^$', 'index', name='linkshare-index'),
    url(r'^post/(?P<post_id>\d+)/$', 'show_post', name='linkshare-show_post'),
    url(r'^add/$', 'add_post', name='linkshare-add_post'),
)
