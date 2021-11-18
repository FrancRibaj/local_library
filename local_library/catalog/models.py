import uuid
from django.db import models
from datetime import date


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(verbose_name='Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = 'author'

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    
    def __str__(self):
        
        return self.first_name + ' ' + self.last_name

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    class Meta:
        db_table = 'genre'

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(models.Model):
    """Represents a Book"""
    title = models.CharField(max_length=200 , null = False, blank = False, help_text = 'Book')
    isbn = models.CharField(verbose_name = 'ISBN',max_length=13, unique=True, help_text = '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    author = models.ManyToManyField(to = 'Author')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book', null=True)
    genre = models.ManyToManyField(to='Genre', help_text='Select a genre for this book')

    class Meta:
        db_table = 'book'
        
    def __str__(self):
        """String for representing the Model object."""
        return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    borrower = models.ForeignKey('accounts.CustomUser', on_delete = models.SET_NULL, null=True, blank =True)
    class Meta:
        ordering = ['due_back']

    @property
    def is_overdue(self):
        if self.due_back and self.status == 'o' and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'