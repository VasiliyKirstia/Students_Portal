from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from library.models import *
from django.contrib.auth.decorators import login_required
from mixins.AccessMixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Q
from django import forms


class HomeView(ListView):
    paginate_by = 20
    context_object_name = 'books_list'
    template_name = 'library/index.html'

    def get_queryset(self):
        return Book.objects.all()

    def post(self, request, *args, **kwargs):
        if 'query' in self.request.POST and self.request.POST['query'] != '':
            query = self.request.POST['query']
            return render(self.request, 'library/index.html',
                          {'books_list': Book.objects.filter(Q(title__contains=query) |
                                                             Q(author__contains=query) |
                                                             Q(imprint_date__contains=query) |
                                                             Q(publisher__contains=query) |
                                                             Q(description__contains=query))[:40]
                          })
        return redirect('library:home')


class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'book_pk'
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'imprint_date', 'description', 'imprint_date', 'tags', 'book_file']
    success_url = reverse_lazy('library:home')
    template_name = 'library/book_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreateView, self).form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'imprint_date', 'description', 'imprint_date', 'tags', 'book_file']
    pk_url_kwarg = 'book_pk'
    success_url = reverse_lazy('library:home')
    template_name = 'library/book_create.html'
