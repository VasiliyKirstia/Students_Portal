from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from films.models import *
from mixins.permissions import LoginRequiredMixin


class FilmsListView(ListView):
    """
    Фильтрует фильмы по категории/автору/"поисковому запросу".
    По умолчанию отображает все фильмы отсортированые по дате добавления.
    """
    paginate_by = 20
    context_object_name = 'films_list'
    template_name = 'films/index.html'

    def get_queryset(self):
        if 'filter_by' in self.kwargs:
            if self.kwargs['filter_by'] == 'category':
                return Film.objects.filter(category=get_object_or_404(Category, pk=self.kwargs['category_pk']))
            elif self.kwargs['filter_by'] == 'author':
                return Film.objects.filter(user=get_object_or_404(User, pk=self.kwargs['user_pk']))
        return Film.objects.all()

    def post(self, request, *args, **kwargs):
        if 'query' in self.request.POST and self.request.POST['query'] != '':
            query = self.request.POST['query']
            return render(self.request, 'films/index.html',
                          {'films_list': Film.objects.filter(Q(title__contains=query) |
                                                             Q(release_date__contains=query) |
                                                             Q(description__contains=query))[:40]})
        return redirect('films:home')


class FilmDetailView(LoginRequiredMixin, DetailView):
    """
    Страница "онлайн просмотра"/скачивания фильма.
    """
    model = Film
    pk_url_kwarg = 'film_pk'
    template_name = 'films/film_detail.html'
    context_object_name = 'film'


class FilmCreateView(LoginRequiredMixin, CreateView):
    """
    Страница добавления нового фильма.
    """
    model = Film
    fields = ['title', 'release_date', 'description', 'category', 'film_file']
    success_url = reverse_lazy('films:home')
    template_name = 'films/film_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FilmCreateView, self).form_valid(form)


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    """
    Страница редактирования фильма.
    """
    model = Film
    fields = ['title', 'release_date', 'description', 'category', 'film_file']
    pk_url_kwarg = 'film_pk'
    success_url = reverse_lazy('films:home')
    template_name = 'films/film_create.html'
