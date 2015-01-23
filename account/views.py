from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, FormView
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect


class RegistrationUser(CreateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'email', 'password']