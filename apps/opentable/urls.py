from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'opentable.views.index', name='index'),
    url(r'^reservation/$', 'opentable.views.reservation', name='reservation'),
    url(r'^reservation/(?P<restaurant_id>\d+)/$', 'opentable.views.reservation', name='reservation'),
    url(r'^restaurants/$', 'opentable.views.restaurants', name='restaurants'),
)
