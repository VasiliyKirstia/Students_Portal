from django.http import Http404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, FormView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from forum.models import *
from django.contrib.auth.decorators import login_required
from mixins.AccessMixins import LoginRequiredMixin
from django.utils.decorators import method_decorator


class TopicList(ListView):
    paginate_by = 20
    context_object_name = 'topic_list'
    template_name = 'forum/index.html'

    def get_queryset(self):
        #TODO выводить темы в порядке от новых к старым
        if 'filter_by' in self.kwargs:
            if self.kwargs['filter_by'] == 'category':
                return Topic.objects.filter(category=get_object_or_404(Category, pk=self.kwargs['category_pk']))
            elif self.kwargs['filter_by'] == 'author':
                return Topic.objects.filter(user=get_object_or_404(User, pk=self.kwargs['user_pk']))
        return Topic.objects.all()


class TopicAnswers(ListView):
    paginate_by = 30
    context_object_name = 'answer_list'
    template_name = 'forum/answers.html'

    def get_queryset(self):
        topic = get_object_or_404(Topic, id=self.kwargs['topic_id'])
        return Answer.objects.filter(topic=topic)

    def get_context_data(self, **kwargs):
        context = super(TopicAnswers, self).get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, id=self.kwargs['topic_id'])
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/login/?next=%s' % request.path)
        answer = Answer(
            text=request.POST['text'],
            topic=get_object_or_404(Topic, id=self.kwargs['topic_id']),
            user=request.user,
        )
        answer.save()
        return redirect(request.path)


class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'text', 'category', 'solved']
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/topic_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
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