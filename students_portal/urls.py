from django.conf.urls import patterns, include, url
from django.contrib import admin
from students_portal import views
from django.conf import settings
from django.conf.urls.static import static
import forum.urls as forum_urls
import account.urls as account_urls
import hallway.urls as hallway_urls
import library.urls as library_urls
import films.urls as films_urls
import chat.urls as chat_urls
import research_work.urls as research_urls

urlpatterns = patterns(
    '',

    url(r'^', include(hallway_urls, namespace='hallway')),

    url(r'^forum/', include(forum_urls, namespace='forum')),

    url(r'^account/', include(account_urls, namespace='account')),

    url(r'^library/', include(library_urls, namespace='library')),

    url(r'^films/', include(films_urls, namespace='films')),

    url(r'^chat/', include(chat_urls, namespace='chat')),

    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^secret_research/', include(research_urls, namespace='research')),

    url(r'^secret_view_404/$', views.error_page_404),

    url(r'^secret_view_500/$', views.error_page_500),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'students_portal.views.error_page_404'

handler500 = 'students_portal.views.error_page_500'