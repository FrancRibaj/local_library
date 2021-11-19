from django.http.response import Http404, HttpResponse 
from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthorsListView(LoginRequiredMixin, generic.ListView):
    model = Author
    template_name = 'authors.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'