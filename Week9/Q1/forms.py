from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(required=False)
    contact_number = forms.CharField(max_length=15, required=False)

class PollForm(forms.Form):
    CHOICES = [
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('bad', 'Bad'),
    ]
    rating = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect, 
        label="How is the book ASP.NET with c# by Vipul Prakashan?"
    )

class CGPAForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    total_marks = forms.IntegerField(label="Total Marks")

from django import forms

class BillForm(forms.Form):
    BRANDS = [
        ('HP', 'HP'),
        ('Nokia', 'Nokia'),
        ('Samsung', 'Samsung'),
        ('Motorola', 'Motorola'),
        ('Apple', 'Apple'),
    ]
    CATEGORIES = [
        ('Mobile', 'Mobile'),
        ('Laptop', 'Laptop'),
    ]
    
    brand = forms.ChoiceField(choices=BRANDS, widget=forms.RadioSelect)
    items = forms.MultipleChoiceField(choices=CATEGORIES, widget=forms.CheckboxSelectMultiple)
    quantity = forms.IntegerField(min_value=1)

from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)

    SUBJECT_CHOICES = [
        ('ASP-XML', 'ASP-XML'),
        ('DotNET', 'DotNET'),
        ('JavaPro', 'JavaPro'),
        ('Unix,C,C++', 'Unix,C,C++'),
    ]
    
    subjects = forms.MultipleChoiceField(
        label="Select Subjects",
        choices=SUBJECT_CHOICES,
        widget=forms.SelectMultiple
    )