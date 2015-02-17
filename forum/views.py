from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django import forms

from forum.models import *
from mixins.decorators import login_required_for_class


#TODO убрать к чертям эту подпорку
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']


class QuestionsList(ListView):
    paginate_by = 20
    context_object_name = 'question_list'
    template_name = 'forum/index.html'

    def get_queryset(self):
        if 'filter_by' in self.kwargs:
            if self.kwargs['filter_by'] == 'category':
                return Question.objects.filter(category=get_object_or_404(Category, pk=self.kwargs['category_pk']))
            elif self.kwargs['filter_by'] == 'author':
                return Question.objects.filter(user=get_object_or_404(User, pk=self.kwargs['user_pk']))
        return Question.objects.all()

    def post(self, request, *args, **kwargs):
        if 'query' in self.request.POST and self.request.POST['query'] != '':
            query = self.request.POST['query']
            return render(self.request, 'forum/index.html',
                          {'question_list': Question.objects.filter(Q(title__contains=query)|Q(text__contains=query))[:40]})
        return redirect('forum:home')


class QuestionAnswers(ListView):
    paginate_by = 30
    context_object_name = 'answer_list'
    template_name = 'forum/answers.html'

    def get_queryset(self):
        question = get_object_or_404(Question, id=self.kwargs['question_id'])
        return Answer.objects.filter(question=question)

    def get_context_data(self, **kwargs):
        context = super(QuestionAnswers, self).get_context_data(**kwargs)
        context['form'] = AnswerForm()
        context['question'] = get_object_or_404(Question, id=self.kwargs['question_id'])
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/account/login/?next=%s' % request.path)
        if request.POST['text'] != '':
            _question = get_object_or_404(Question, id=self.kwargs['question_id'])
            answer = Answer(
                text=request.POST['text'],
                question=_question,
                user=request.user,
            )
            answer.save()
            #TODO еще один костылец
            _question.answers_count += 1
            _question.save()
        #TODO Настроить редирект так, чтоб он отсылал на ту же самую страницу с которой пришел пользователь без использования костыля
        return redirect(request.path + '?page=last')


@login_required_for_class
class QuestionCreate(CreateView):
    model = Question
    fields = ['title', 'text', 'category', 'solved']
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/question_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuestionCreate, self).form_valid(form)


@login_required_for_class
class QuestionUpdate(UpdateView):
    model = Question
    fields = ['title', 'text', 'category', 'solved']
    pk_url_kwarg = 'question_id'
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/question_create.html'


@login_required_for_class
class QuestionDelete(DeleteView):
    model = Question
    pk_url_kwarg = 'question_id'
    success_url = reverse_lazy('forum:home')
    template_name = 'forum/question_delete.html'