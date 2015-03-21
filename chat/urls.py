from django.conf.urls import patterns, url
from chat.views import *

urlpatterns = patterns(
    '',
    url(r'^$', RoomsListView.as_view(), name='home'),
    url(r'^room/(?P<room_pk>\d+)/$', RoomDetailView.as_view(), name='room'),
    url(r'^create/room/', RoomCreateView.as_view(), name='create'),

    url(r'^send/$', 'chat.views.send'),
    url(r'^receive/$', 'chat.views.receive'),
    url(r'^sync/$', 'chat.views.sync'),

    url(r'^join/$', 'chat.views.join'),
    url(r'^leave/$', 'chat.views.leave'),
)