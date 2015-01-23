from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, FormView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from forum.models import *


class TopicList(ListView):
    paginate_by = 20
    context_object_name = 'topic_list'
    template_name = 'forum/index.html'

    def get_queryset(self):
        try:
            category = get_object_or_404(Category, id=self.kwargs['category_id'])
            return Topic.objects.filter(category=category)
        except KeyError:
            return Topic.objects.all()


class TopicAnswers(ListView, FormView):
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
        return redirect(request.path)


class TopicCreate(CreateView):
    model = Topic
    fields = ['title', 'text', 'category', 'author', 'solved']
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/topic_create.html'

    def form_valid(self, form):
        return super(TopicCreate, self).form_valid(form)


class TopicUpdate(UpdateView):
    model = Topic
    fields = ['title', 'text', 'category', 'solved']
    pk_url_kwarg = 'topic_id'
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/topic_create.html'


class TopicDelete(DeleteView):
    model = Topic
    pk_url_kwarg = 'topic_id'
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/topic_delete.html'