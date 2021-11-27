from django.urls import path
from catalog.views.book_instance import LoanedBooksByUserListView
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('books/', views.BookListView.as_view(), name = 'books'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('books/create/', views.create_book, name='create-book'),
    path('authors/', views.AuthorsListView.as_view(), name = 'authors'),
    path('authors/create', views.create_author, name = 'create-author'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name = 'author-detail'),
    path('borrowed-books/', views.LoanedBooksByUserListView.as_view(), name = 'borrowed-books'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]