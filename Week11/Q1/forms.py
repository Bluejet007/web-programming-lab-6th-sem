from django import forms
from .models import Product, Book, Student

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'authors', 'publisher']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'course', 'dob']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }