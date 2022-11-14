from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre, Language


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'mum_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        num_visits: num_visits,
    }


    return render(request, 'index.html', context=context)


class BooksListView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BooksListView, self).get_context_data(**kwargs)
        context['Some_data'] = 'This is just some data'
        return context

    def get_queryset(self):
        return Book.objects.filter(title='war')[:5]

    template_name = 'books/my_arbitrary_template_name_list.html'


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Book