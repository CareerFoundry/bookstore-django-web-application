from django.shortcuts import render                     #imported by default
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Book                                #to access Book model

# Create your views here.
class BookListView(ListView):                           #class-based view
    model = Book                                        #specify model
    template_name = 'books/main.html'                   #specify template

class BookDetailView(DetailView):                       #class-based view
    model = Book                                        #specify model
    template_name = 'books/detail.html'                 #specify template
