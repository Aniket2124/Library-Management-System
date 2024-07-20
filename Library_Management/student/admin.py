from django.contrib import admin
from .models import Author, Book, Borrower, Borrowing

# Register your models here.
admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'nationality']

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'year_of_publication', 'genre']

admin.site.register(Borrower)

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number']

admin.site.register(Borrowing)

class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['borrower', 'book', 'date_borrowed', 'due_date', 'date_return']
