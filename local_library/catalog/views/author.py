from django.shortcuts import redirect,  render
from catalog.forms import AuthorForm
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

def create_author(request):
    if request.method == 'Post':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = Author.objects.create(
            first_name =form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            date_of_birth=form.cleaned_data['date_of_birth'],
            date_of_death=form.cleaned_data['date_of_death'],
            )
        return redirect('authors')

    else:
        form = AuthorForm()
        context = {'forms':form}
        return render (request,'create_author.html',context)