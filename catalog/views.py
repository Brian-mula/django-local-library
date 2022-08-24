from django.shortcuts import render
from .models import Book,BookInstance,Author,Genre
# Create your views here.

def index(request):
    """views function for the home page of the site"""
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # available books
    num_instance_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    num_genre=Genre.objects.count()
    page_title='Local library'

    context={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instance_available':num_instance_available,
        'num_authors':num_authors,
        'page_title':page_title,
        'num_genre':num_genre
    }

    # render the html index with data in context
    return render(request,'index.html',context=context)

def allbooks(request):
    content="This is the books page"
    page_title="All Books"
    context={
        'content':content,
        'page_title':page_title
    }
    return render(request,'books.html',context=context)