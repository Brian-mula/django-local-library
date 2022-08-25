
from re import L
from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date




# Create your models here.

class Genre(models.Model):
    """model representing a book genre"""
    name=models.CharField(max_length=200,help_text='enter a book genre (eg Science Fiction)')

    def __str__(self):
        """string for representing a model object"""
        return self.name


class Book(models.Model):
    """a class representing a book model but not a specific book"""
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary=models.TextField(max_length=1000,help_text="Enter a brief description of the book")
    isbn=models.CharField('ISBN',max_length=13,unique=True,help_text='13 characters')
    genre=models.ManyToManyField(Genre,help_text='select a genre for this book')

    def __str__(self):
        """string representation for model object"""
        return self.title

    def get_absolute_url(self):
        """returns URL to access a detailed record for this book"""
        return reverse('book-detail',args=[str(self.id)])

    def display_genre(self):
        """create a string for genre"""
        return ','.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description= 'Genre'

    
class BookInstance(models.Model):
    """model representing a specific copy of the book"""
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='unique id for the book accross the library')
    book=models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)
    borrower=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    LOAN_STATUS=(
        ('m','Maintenance'),
        ('o', 'On loan'),
       ( 'a','available'),
        ('r','Reserved')
    )
    status=models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text="Book availability"
    )
    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)

    class Meta:
        ordering=['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    """model representing the author"""
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)

    class Meta:
        ordering=['last_name','first_name']

    def get_absolute_url(self):
        """returns a URL to acces a particular author"""
        return reverse ('author-detail',args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name} '