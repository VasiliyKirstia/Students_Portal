from django.conf.urls import patterns, include, url
import portal.views as views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='home'),
)