from django.shortcuts import render
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from books.models import Book
# Create your views here.

# listView
# DetailView

class create_book(CreateView):
    model = Book
    fields = "__all__"
    template_name = "books/book_form.html"
