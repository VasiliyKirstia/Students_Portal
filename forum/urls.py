from django.conf.urls import patterns, include, url
from forum.views import *

urlpatterns = patterns(
    '',
    url(r'^$', TopicList.as_view(), name='home'),
    url(r'^(?P<category_id>\d+)/$', TopicList.as_view(), name='home'),
    url(r'^detail/(?P<topic_id>\d+)/$', TopicDetail.as_view(), name='detail'),
    url(r'^topic/create/$', TopicCreate.as_view(), name='create_topic'),
    url(r'^topic/(?P<topic_id>\d+)/update/$', TopicUpdate.as_view(), name='update_topic'),
    url(r'^topic/(?P<topic_id>\d+)/delete/$', TopicDelete.as_view(), name='delete_topic'),
)