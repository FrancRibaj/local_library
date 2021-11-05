from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('Hello/', views.hello, name = 'hello'),
    path('books/', views.BookListView.as_view(), name='books')
]