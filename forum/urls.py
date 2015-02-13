from django.conf.urls import patterns, include, url
from forum.views import *


urlpatterns = patterns(
    '',
    url(r'^$', QuestionsList.as_view(), name='home'),

    url(r'^by_category/(?P<category_pk>\d+)/$', QuestionsList.as_view(), {'filter_by': 'category'}, name='by-category'),

    url(r'^by_author/(?P<user_pk>\d+)/$', QuestionsList.as_view(), {'filter_by': 'author'}, name='by-author'),

    url(r'^question/(?P<question_id>\d+)/answers/$', QuestionAnswers.as_view(), name='answers'),

    url(r'^question/create/$', QuestionCreate.as_view(), name='create_question'),

    url(r'^question/(?P<question_id>\d+)/edit/$', QuestionUpdate.as_view(), name='update_question'),

    url(r'^question/(?P<question_id>\d+)/delete/$', QuestionDelete.as_view(), name='delete_question'),
)


