from django.shortcuts import render, redirect
from .models import Category, Page, Works, Lives, Institutes
from .forms import CategoryForm, PageForm, WorksForm, CompanySearchForm

def Q1(req):
    categories = Category.objects.all()
    pages = Page.objects.all()
    
    return render(req, 'index.html', {
        'categories': categories,
        'pages': pages
    })

def Q1_category(req):
    form = CategoryForm()
    
    if req.method == 'POST':
        form = CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(req, 'add_category.html', {'form': form})


def Q1_page(req):
    form = PageForm()
    
    if req.method == 'POST':
        form = PageForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(req, 'add_page.html', {'form': form})

def add_work(req):
    form = WorksForm()

    if req.method == 'POST':
        form = WorksForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('add_work')

    return render(req, 'add_work.html', {'form': form})


def search_company(req):
    form = CompanySearchForm()
    results = []

    if req.method == 'POST':
        form = CompanySearchForm(req.POST)
        if form.is_valid():
            company = form.cleaned_data['company_name']

            works_people = Works.objects.filter(company_name=company)

            for w in works_people:
                try:
                    city = Lives.objects.get(person_name=w.person_name).city
                except Lives.DoesNotExist:
                    city = "Oslo"

                results.append({
                    'name': w.person_name,
                    'city': city
                })

    return render(req, 'search.html', {
        'form': form,
        'results': results
    })

def A1(req):
    institutes = Institutes.objects.all()
    return render(req, 'A1.html', {
        'institutes': institutes
    })