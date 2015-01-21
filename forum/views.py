from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from forum.models import *


class TopicList(ListView):
    context_object_name = 'topic_list'
    template_name = 'forum/index.html'

    def get_queryset(self):
        try:
            category = get_object_or_404(Category, id=self.kwargs['category_id'])
            return Topic.objects.filter(category=category)
        except KeyError:
            return Topic.objects.all()


class TopicDetail(DetailView):
    model = Topic
    pk_url_kwarg = 'topic_id'
    template_name = 'forum/detail.html'

    def get_context_data(self, **kwargs):
        context = super(TopicDetail, self).get_context_data(**kwargs)
        context['answer_list'] = Answer.objects.filter(topic=self.object)
        return context

class TopicCreate(CreateView):
    model = Topic
    fields = ['title', 'text', 'date', 'category', 'author', 'solved']
    template_name = 'forum/create.html'
