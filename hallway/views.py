from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from hallway.models import *
from django.contrib.auth.decorators import login_required
from mixins.AccessMixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Q
from datetime import datetime

class HomeView(TemplateView):
    template_name = 'hallway/index.html'

class RulesView(TemplateView):
    def get(self, request):
        return render(request, 'hallway/rules.html', {'rules': Rules.objects.get()})
