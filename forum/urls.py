from django.conf.urls import patterns, include, url
import forum.views as views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='home'),
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
)