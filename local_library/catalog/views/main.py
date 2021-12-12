from django.http.response import Http404, HttpResponse 
from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def hello(request):
    return HttpResponse('Hello!!!')

def index(request):
    """View function for home page of site."""
    if request.user.is_authenticated:
    
        num_visits = request.session.get('num_visits', 0)

        # Generate counts of some of the main objects
        request.session['num_visits'] = num_visits + 1
        num_books = Book.objects.all().count()
        print(Book.objects.all().count())
        num_instances = BookInstance.objects.all().count()

        # Available books (status = 'a')
        num_instances_available = BookInstance.objects.filter(status__exact='a').count()

        # The 'all()' is implied by default.
        num_authors = Author.objects.count()

        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_visits': num_visits
        }
    else:
        context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)