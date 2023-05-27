from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView): 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data()
        
    #     context['books'] = Book.objects.all()
    #     return context

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
