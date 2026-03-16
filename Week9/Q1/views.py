from django.shortcuts import render, redirect
from .forms import RegistrationForm, PollForm, CGPAForm, BillForm, FeedbackForm

def Q1_reg_view(req):
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            context = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'contact_number': form.cleaned_data['contact_number'],
            }
            return render(req, 'Q1_suc.html', context)
    else:
        form = RegistrationForm()
    
    return render(req, 'Q1_reg.html', {'form': form})

def Q2_view(req):
    if req.method == 'POST':
        form = PollForm(req.POST)
        if form.is_valid():
            results = {
                'good_pct': 70,
                'satisfactory_pct': 20,
                'bad_pct': 10,
                'voted': True
            }
            return render(req, 'Q2.html', results)
    else:
        form = PollForm()
    
    return render(req, 'Q2.html', {'form': form, 'voted': False})

def Q3_view(req):
    if req.method == 'POST':
        form = CGPAForm(req.POST)
        if form.is_valid():
            req.session['user_name'] = form.cleaned_data['name']
            req.session['total_marks'] = form.cleaned_data['total_marks']
            return redirect('Q3_res')
    else:
        form = CGPAForm()
    return render(req, 'Q3.html', {'form': form})

def Q3_res_view(req):
    name = req.session.get('user_name', 'Guest')
    marks = req.session.get('total_marks', 0)

    cgpa = marks / 50
    
    return render(req, 'Q3_res.html', {'name': name, 'cgpa': cgpa})

def A1_view(req):
    if req.method == 'POST':
        form = BillForm(req.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            selected_items = form.cleaned_data['items']
            qty = form.cleaned_data['quantity']

            prices = {'Mobile': 15000, 'Laptop': 50000}
            unit_price = sum(prices[item] for item in selected_items)
            total_amount = unit_price * qty

            context = {
                'brand': brand,
                'items': ", ".join(selected_items),
                'quantity': qty,
                'total': total_amount
            }
            return render(req, 'A1_bill.html', context)
    else:
        form = BillForm()

    return render(req, 'A1.html', {'form': form})

def A2_view(req):
    message = ""
    if req.method == 'POST':
        form = FeedbackForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            selected_list = form.cleaned_data['subjects']
            
            # Formatting the list for the message
            subjects_str = ", ".join(selected_list)
            message = f"Hello {name}, your feedback for {subjects_str} is submitted successfully."
    else:
        form = FeedbackForm()

    return render(req, 'A2.html', {'form': form, 'message': message})