from django.conf.urls import patterns, include, url
from django.contrib import admin

from portal import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'students_portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
