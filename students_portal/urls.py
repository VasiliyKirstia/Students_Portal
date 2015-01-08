from django.conf.urls import patterns, include, url
from django.contrib import admin

import portal.urls as urls_from_portal
import forum.urls as urls_from_forum
from portal.views import index as home

urlpatterns = patterns(
    '',
    url(r'^$', home, name='home'),
    url(r'^portal/', include(urls_from_portal, namespace='portal')),
    url(r'^forum/', include(urls_from_forum, namespace='forum')),
#    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
