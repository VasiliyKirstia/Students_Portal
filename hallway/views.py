from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import redirect, render
from django.db.models import Q
from django import forms

from hallway.models import *
from mixins.permissions import LoginRequiredMixin
from mixins.forms import SuggestionForm


class HomeView(ListView):
    paginate_by = 20
    context_object_name = 'news_list'
    template_name = 'hallway/index.html'

    def get_queryset(self):
        return News.objects.all()

    def post(self, request, *args, **kwargs):
        if 'query' in self.request.POST and self.request.POST['query'] != '':
            query = self.request.POST['query']
            return render(self.request, 'hallway/index.html',
                          {'news_list': News.objects.filter(Q(title__contains=query) | Q(text__contains=query))[:40]})
        return redirect('hallway:home')


class RulesView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'hallway/rules.html', {'rules': Rules.objects.get()})


class NewsDetailView(DetailView):
    model = News
    pk_url_kwarg = 'news_pk'
    template_name = 'hallway/news_detail.html'
    context_object_name = 'news'


class DevelopersDetailView(ListView):
    model = Developer
    template_name = 'hallway/developers_detail.html'
    context_object_name = 'developers_list'


class SuggestionCreate(LoginRequiredMixin, ListView):
    paginate_by = 30
    model = Suggestion
    context_object_name = 'suggestions_list'
    template_name = 'hallway/suggestions.html'

    def get_context_data(self, **kwargs):
        context = super(SuggestionCreate, self).get_context_data(**kwargs)
        context['form'] = SuggestionForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SuggestionForm(request.POST)
        form.instance.user = self.request.user
        if form.is_valid():
            form.save()
        # TODO Настроить редирект так, чтоб он отсылал на ту же самую страницу с которой пришел
        return redirect(request.path)