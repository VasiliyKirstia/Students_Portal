from django.conf.urls import patterns, include, url
from hallway.views import *


urlpatterns = patterns(
    '',

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^rules/$', RulesView.as_view(), name='rules'),
)