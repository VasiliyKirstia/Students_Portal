from django.conf.urls import patterns, url

from library.views import *


urlpatterns = patterns(
    '',

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^by_category/(?P<category_pk>\d+)/$', HomeView.as_view(), {'filter_by': 'category'}, name='by-category'),

    url(r'^by_author/(?P<user_pk>\d+)/$', HomeView.as_view(), {'filter_by': 'author'}, name='by-author'),

    url(r'^book/(?P<book_pk>\d+)/detail/$', BookDetailView.as_view(), name='detail'),

    url(r'^book/add/$', BookCreateView.as_view(), name='add'),

    url(r'^book/(?P<book_pk>\d+)/update/$', BookUpdateView.as_view(), name='update'),
)
