from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, FormView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from forum.models import *
from django import forms


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


class TopicDetail(DetailView):
    model = Topic
    pk_url_kwarg = 'topic_id'
    template_name = 'forum/detail.html'

    form_class = Answer
    success_url = reverse_lazy('forum:detail')

    def get_context_data(self, **kwargs):
        context = super(TopicDetail, self).get_context_data(**kwargs)
        context['answer_list'] = Answer.objects.filter(topic=self.object)
        return context


class TopicCreate(CreateView):
    model = Topic
    fields = ['title', 'text', 'date', 'category', 'author', 'solved']
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/create.html'

class TopicUpdate(UpdateView):
    model = Topic
    fields = ['title', 'text', 'date', 'category', 'solved']
    pk_url_kwarg = 'topic_id'
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/create.html'

class TopicDelete(DeleteView):
    model = Topic
    pk_url_kwarg = 'topic_id'
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/delete.html'


class TopicForm(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeField(widget=forms.DateTimeBaseInput)
    category = forms.InlineForeignKeyField(Category)
    author = forms.InlineForeignKeyField(Author)
    solved = forms.CheckboxInput