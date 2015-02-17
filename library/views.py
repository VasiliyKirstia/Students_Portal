from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from library.models import *
from mixins.decorators import login_required_for_class


class HomeView(ListView):
    paginate_by = 20
    context_object_name = 'books_list'
    template_name = 'library/index.html'

    def get_queryset(self):
        if 'filter_by' in self.kwargs:
            if self.kwargs['filter_by'] == 'category':
                return Book.objects.filter(category=get_object_or_404(Category, pk=self.kwargs['category_pk']))
            elif self.kwargs['filter_by'] == 'author':
                return Book.objects.filter(user=get_object_or_404(User, pk=self.kwargs['user_pk']))
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


@login_required_for_class
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'imprint_date', 'description', 'imprint_date', 'category', 'book_file']
    success_url = reverse_lazy('library:home')
    template_name = 'library/book_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreateView, self).form_valid(form)


@login_required_for_class
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'imprint_date', 'description', 'imprint_date', 'category', 'book_file']
    pk_url_kwarg = 'book_pk'
    success_url = reverse_lazy('library:home')
    template_name = 'library/book_create.html'
