from django.conf.urls import patterns, include, url
import forum.views as views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='home'),
    url(r'^(?P<category_id>\d+)/$', views.index, name='home'),
    url(r'^detail/(?P<topic_id>\d+)/$', views.detail, name='detail'),
)