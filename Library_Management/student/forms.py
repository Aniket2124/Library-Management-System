from django import forms
from .models import Author, Book, Borrower, Borrowing

class Author_Creation_Form(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Date Of Birth'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'biography': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BioGraphy'}),
        }


class Book_Creation_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Published Date'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre'}),
        }