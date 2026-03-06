from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    ordering = ['-pub_date']


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
