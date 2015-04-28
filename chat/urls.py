from django.conf.urls import patterns, url
from chat.views import *

urlpatterns = patterns(
    '',
    url(r'^init/$', init),
    url(r'^active_sync/$', active_sync),
    url(r'^passive_sync', passive_sync),

    url(r'^send_message/$', send_message),
    url(r'^send_invites/$', send_invites),
    url(r'^remove_invite/$', remove_invite),
    url(r'^create_room/$', create_room),

    url(r'^join/$', join),
    url(r'^leave/$', leave),
)