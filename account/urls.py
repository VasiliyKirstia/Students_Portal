from django.conf.urls import patterns, include, url
from account.views import *

urlpatterns = patterns(
    '',
    url(r'^registration/$', RegistrationUser.as_view(), name='registration'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
)