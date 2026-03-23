from django import forms
from .models import Category, Page, Works

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'url', 'category')

class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['person_name', 'company_name', 'salary']

class CompanySearchForm(forms.Form):
    company_name = forms.CharField(max_length=100)