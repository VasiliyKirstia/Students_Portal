from django.conf.urls import patterns, include, url
from library.views import *


urlpatterns = patterns(
    '',

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^book/(?P<book_pk>\d+)/detail/$', BookDetailView.as_view(), name='detail'),

    url(r'^book/add/$', BookCreateView.as_view(), name='add'),

    url(r'^book/update/$', BookUpdateView.as_view(), name='update'),
)
