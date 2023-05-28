from django.views.generic import ListView, DetailView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class BookListView(LoginRequiredMixin, ListView): 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data()
        
    #     context['books'] = Book.objects.all()
    #     return context

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
