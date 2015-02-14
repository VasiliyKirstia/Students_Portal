from django.conf.urls import patterns, include, url
from films.views import *


urlpatterns = patterns(
    '',

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^film/(?P<film_pk>\d+)/detail/$', FilmDetailView.as_view(), name='detail'),

    url(r'^film/add/$', FilmCreateView.as_view(), name='add'),

    url(r'^film/update/$', FilmUpdateView.as_view(), name='update'),
)