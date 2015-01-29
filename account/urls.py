from django.conf.urls import patterns, include, url
from account.views import *

urlpatterns = patterns(
    '',
    url(r'^registration/$', RegistrationUser.as_view(), name='registration'),
    url(r'^login/$', log_in, name='login'),
    url(r'^logout/$', log_out, name='logout'),
)