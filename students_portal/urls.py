from django.conf.urls import patterns, include, url
from django.contrib import admin

import forum.urls as urls_from_forum

urlpatterns = patterns(
    '',
    #url(r'^$', home, name='home'),
    url(r'^forum/', include(urls_from_forum, namespace='forum')),
    url(r'^admin/', include(admin.site.urls)),
)

