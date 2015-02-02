from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from hallway.models import *
from django.contrib.auth.decorators import login_required
from mixins.AccessMixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Q
from datetime import datetime


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
                          {'news_list': News.objects.filter(Q(title__contains=query)|Q(text__contains=query))[:40]})
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

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/login/?next=%s' % request.path)
        if request.POST['text'] != '':
            suggestion = Suggestion(
                text=request.POST['text'],
                date=datetime.now(),
                user=request.user,
            )
            suggestion.save()
        #TODO Настроить редирект так, чтоб он отсылал на ту же самую страницу с которой пришел пользователь без использования костыля
        return redirect(request.path + '?page=last')