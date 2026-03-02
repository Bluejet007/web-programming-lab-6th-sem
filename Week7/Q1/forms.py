from django import forms

class Q1_form(forms.Form):
    MANUFACTURERS = [
        ('Toyota', 'Toyota'),
        ('BMW', 'BMW'),
        ('Tesla', 'Tesla'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
    ]
    
    manufact = forms.ChoiceField(choices=MANUFACTURERS)
    mod_name = forms.CharField(max_length=100)

class Q2_form(forms.Form):
    SUBJECTS = [
        ('Math', 'Math'),
        ('English', 'English'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
    ]
    name = forms.CharField(max_length=100)
    roll = forms.CharField(max_length=100)
    subject = forms.ChoiceField(choices=SUBJECTS)

class A1_form(forms.Form):
    ITEMS = [
        ('wheat', 'Wheat', 40),
        ('jaggery', 'Jaggery', 60),
        ('dal', 'Dal', 80),
    ]

    wheat = forms.BooleanField(required=False, label='Wheat')
    jaggery = forms.BooleanField(required=False, label='Jaggery')
    dal = forms.BooleanField(required=False, label='Dal')