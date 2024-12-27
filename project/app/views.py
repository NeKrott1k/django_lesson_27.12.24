from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')
    
class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete_confirm.html'
    success_url = reverse_lazy('book-list')
    context_object_name = 'book'