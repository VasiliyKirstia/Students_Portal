from django.conf.urls import patterns, include, url
from django.contrib import admin
import forum.urls as forum_urls
import account.urls as account_urls
import hallway.urls as hallway_urls
from students_portal import views

urlpatterns = patterns(
    '',

    url(r'^', include(hallway_urls, namespace='hallway')),

    url(r'^forum/', include(forum_urls, namespace='forum')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/', include(account_urls, namespace='account')),

    (r'^ckeditor/', include('ckeditor.urls')),

    url(r'^secret_view_404/$', views.error_page_404),

    url(r'^secret_view_500/$', views.error_page_500),
)

handler404 = 'students_portal.views.error_page_404'

handler500 = 'students_portal.views.error_page_500'