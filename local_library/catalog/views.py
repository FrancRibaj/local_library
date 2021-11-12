from django.http.response import Http404, HttpResponse 
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.
from .models import Book, Author, BookInstance, Genre
from django.views import generic 

def index(request):
    """View function for home page of site."""
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

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def hello(request):
    return HttpResponse('Hello!!!')

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = "books.html"
    

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

def book_detail(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404   
    return render(request, 'book_detail.html', context ={ 'book': book} )

class AuthorsListView(generic.ListView):
    model = Author
    template_name = 'authors.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
