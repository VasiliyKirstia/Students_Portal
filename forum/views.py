from django.http import Http404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, FormView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from forum.models import *
from django.contrib.auth.decorators import login_required
from mixins.AccessMixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Q
from datetime import datetime
from django import forms

#TODO убрать к чертям эту подпорку
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']


class TopicList(ListView):
    paginate_by = 20
    context_object_name = 'topic_list'
    template_name = 'forum/index.html'

    def get_queryset(self):
        if 'filter_by' in self.kwargs:
            if self.kwargs['filter_by'] == 'category':
                return Topic.objects.filter(category=get_object_or_404(Category, pk=self.kwargs['category_pk']))
            elif self.kwargs['filter_by'] == 'author':
                return Topic.objects.filter(user=get_object_or_404(User, pk=self.kwargs['user_pk']))
        return Topic.objects.all()

    def post(self, request, *args, **kwargs):
        if 'query' in self.request.POST and self.request.POST['query'] != '':
            query = self.request.POST['query']
            return render(self.request, 'forum/index.html',
                          {'topic_list': Topic.objects.filter(Q(title__contains=query)|Q(text__contains=query))[:40]})
        return redirect('forum:home')


class TopicAnswers(ListView):
    paginate_by = 30
    context_object_name = 'answer_list'
    template_name = 'forum/answers.html'

    def get_queryset(self):
        topic = get_object_or_404(Topic, id=self.kwargs['topic_id'])
        return Answer.objects.filter(topic=topic)

    def get_context_data(self, **kwargs):
        context = super(TopicAnswers, self).get_context_data(**kwargs)
        context['form'] = AnswerForm()
        context['topic'] = get_object_or_404(Topic, id=self.kwargs['topic_id'])
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/login/?next=%s' % request.path)
        if request.POST['text'] != '':
            answer = Answer(
                text=request.POST['text'],
                date=datetime.now(),
                topic=get_object_or_404(Topic, id=self.kwargs['topic_id']),
                user=request.user,
            )
            answer.save()
        #TODO Настроить редирект так, чтоб он отсылал на ту же самую страницу с которой пришел пользователь без использования костыля
        return redirect(request.path + '?page=last')


class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'text', 'category', 'solved']
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/topic_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date =datetime.now()
        return super(TopicCreate, self).form_valid(form)


class TopicUpdate(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = ['title', 'text', 'category', 'solved']
    pk_url_kwarg = 'topic_id'
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/topic_create.html'


class TopicDelete(LoginRequiredMixin, DeleteView):
    model = Topic
    pk_url_kwarg = 'topic_id'
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/topic_delete.html'