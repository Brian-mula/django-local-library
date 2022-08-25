from django.shortcuts import render
from .models import Book,BookInstance,Author,Genre
from django.views import generic
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
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits + 1

    context={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instance_available':num_instance_available,
        'num_authors':num_authors,
        'page_title':page_title,
        'num_genre':num_genre,
        'num_visits':num_visits
    }

    # render the html index with data in context
    return render(request,'index.html',context=context)

class BookListView(generic.ListView):
    model=Book
    
    
class BookDetailView(generic.DetailView):
    model=Book

class AuthorsView(generic.ListView):
    model=Author

class AuthorDetailView(generic.DetailView):
    model=Author