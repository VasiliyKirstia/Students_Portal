import django.conf.urls
from account.views import *

urlpatterns = django.conf.urls.patterns(
    '',
    django.conf.urls.url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    django.conf.urls.url(r'^login/$', log_in, name='login'),
    django.conf.urls.url(r'^logout/$', log_out, name='logout'),
)