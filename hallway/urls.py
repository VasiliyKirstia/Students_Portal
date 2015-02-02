from django.conf.urls import patterns, include, url
from hallway.views import *


urlpatterns = patterns(
    '',

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^rules/$', RulesView.as_view(), name='rules'),

    url(r'^news/(?P<news_pk>\d+)/', NewsDetailView.as_view(), name='news'),

    url(r'^developers/', DevelopersDetailView.as_view(), name='developers'),

    url(r'^suggestions/', SuggestionCreate.as_view(), name='suggestions'),
)