from django.conf.urls import patterns, include, url
from django.contrib import admin
from students_portal import views
import forum.urls as forum_urls
import account.urls as account_urls
import hallway.urls as hallway_urls
import library.urls as library_urls

urlpatterns = patterns(
    '',

    url(r'^', include(hallway_urls, namespace='hallway')),

    url(r'^forum/', include(forum_urls, namespace='forum')),

    url(r'^account/', include(account_urls, namespace='account')),

    url(r'^library/', include(library_urls, namespace='library')),

    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^secret_view_404/$', views.error_page_404),

    url(r'^secret_view_500/$', views.error_page_500),
)

handler404 = 'students_portal.views.error_page_404'

handler500 = 'students_portal.views.error_page_500'