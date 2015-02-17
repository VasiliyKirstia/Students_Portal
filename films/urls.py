from django.conf.urls import patterns, url

from films.views import *


urlpatterns = patterns(
    '',

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^by_category/(?P<category_pk>\d+)/$', HomeView.as_view(), {'filter_by': 'category'}, name='by-category'),

    url(r'^by_author/(?P<user_pk>\d+)/$', HomeView.as_view(), {'filter_by': 'author'}, name='by-author'),

    url(r'^film/(?P<film_pk>\d+)/detail/$', FilmDetailView.as_view(), name='detail'),

    url(r'^film/add/$', FilmCreateView.as_view(), name='add'),

    url(r'^film/(?P<film_pk>\d+)/update/$', FilmUpdateView.as_view(), name='update'),
)