from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'chat.views.test', name='home'),
    url(r'^send/$', 'chat.views.send'),
    url(r'^receive/$', 'chat.views.receive'),
    url(r'^sync/$', 'chat.views.sync'),

    url(r'^join/$', 'chat.views.join'),
    url(r'^leave/$', 'chat.views.leave'),
)