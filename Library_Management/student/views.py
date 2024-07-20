#Django Imports
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from .forms import Author_Creation_Form, Book_Creation_Form
from django.views import View
from .models import Author, Book, Borrower, Borrowing

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'student/home.html')
#Author Management:

class Author_Creation(CreateView):
    form_class = Author_Creation_Form
    template_name = 'student/author_creation.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Book_Creation(CreateView):
    model = Book
    form_class = Book_Creation_Form
    template_name = 'student/book_creation.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Book_Update(UpdateView):
    model = Book
    form_class = Book_Creation_Form
    template_name = 'student/book_update.html'
    success_url = '/book_list/'


class Book_Details(DetailView):
    model = Book
    template_name = 'student/book_details.html'
    success_url = '/'


class Book_List(ListView):
    model = Book
    template_name = 'student/books.html'

class Book_Delete(DeleteView):
    model = Book
    template_name = 'student/book_delete.html'
    success_url = '/book_list/'
