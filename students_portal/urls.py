from django.conf.urls import patterns, include, url
from django.contrib import admin
import forum.urls as forum_urls
import account.urls as account_urls

urlpatterns = patterns(
    '',
    #url(r'^$', home, name='home'),
    url(r'^forum/', include(forum_urls, namespace='forum')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include(account_urls, namespace='account')),
)

