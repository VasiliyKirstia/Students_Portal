from django.conf.urls import patterns, include, url
from forum.views import *


urlpatterns = patterns(
    '',
    url(r'^$', TopicList.as_view(), name='home'),

    url(r'^by_category/(?P<category_pk>\d+)/$', TopicList.as_view(), {'filter_by': 'category'}, name='by-category'),

    url(r'^by_author/(?P<user_pk>\d+)/$', TopicList.as_view(), {'filter_by': 'author'}, name='by-author'),

    url(r'^topic/(?P<topic_id>\d+)/answers/$', TopicAnswers.as_view(), name='answers'),

    url(r'^topic/create/$', TopicCreate.as_view(), name='create_topic'),

    url(r'^topic/(?P<topic_id>\d+)/edit/$', TopicUpdate.as_view(), name='update_topic'),

    url(r'^topic/(?P<topic_id>\d+)/delete/$', TopicDelete.as_view(), name='delete_topic'),
)


