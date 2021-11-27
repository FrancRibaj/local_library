from django.http.response import Http404, HttpResponse 
from django.shortcuts import redirect, render
from catalog.forms import BookModelForm
from catalog.models import Book, Author, BookInstance, Genre

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(LoginRequiredMixin ,generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = "books.html"

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

@login_required
def book_detail(request, pk):
    try:
         book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404   
    return render(request, 'book_detail.html', context ={ 'book': book} )


def create_book(request):
    if request.method == 'POST':
        form =BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookModelForm()
        context =  {'form':form}
        return render(request, 'create_book.html', context)