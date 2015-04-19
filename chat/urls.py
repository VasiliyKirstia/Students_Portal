from django.conf.urls import patterns, url
from chat.views import *

urlpatterns = patterns(
    '',
    url(r'^init/$', init),
    url(r'^active_sync/$', active_sync),
    url(r'^passive_sync', passive_sync),

    url(r'^send/$', send),
    url(r'^invitation/$', invitation),
    url(r'^remove_invite/$', remove_invite),
    url(r'^create_room/$', create_room),

    url(r'^join/$', join),
    url(r'^leave/$', leave),
)