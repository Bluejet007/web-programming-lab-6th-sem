from django.shortcuts import render, redirect, get_object_or_404, redirect
from .forms import ProductForm, BookForm, StudentForm
from .models import Product, Human, Book, Student

def Q1(request):
    products = Product.objects.all()
    return render(request, 'Q1_index.html', {'products': products})

def Q1_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()

    return render(request, 'Q1_product.html', {'form': form})

def Q2(request):
    humans = Human.objects.all()

    selected_human = None

    # When dropdown changes
    if request.method == 'GET' and 'human_id' in request.GET:
        selected_human = get_object_or_404(Human, id=request.GET.get('human_id'))

    # Update
    if request.method == 'POST' and 'update' in request.POST:
        human = get_object_or_404(Human, id=request.POST.get('human_id'))
        human.first_name = request.POST.get('first_name')
        human.last_name = request.POST.get('last_name')
        human.phone = request.POST.get('phone')
        human.address = request.POST.get('address')
        human.city = request.POST.get('city')
        human.save()
        return redirect(f'/?human_id={human.id}')

    # Delete
    if request.method == 'POST' and 'delete' in request.POST:
        human = get_object_or_404(Human, id=request.POST.get('human_id'))
        human.delete()
        return redirect('/')

    return render(request, 'Q2_index.html', {
        'humans': humans,
        'selected': selected_human
    })

def Q3(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()

    return render(request, 'Q3_index.html', {
        'form': form,
        'books': books
    })

def A1(request):
    students = Student.objects.all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()

    return render(request, 'A1_index.html', {
        'form': form,
        'students': students
    })