from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from .forms import Q1_form, Q2_form, A1_form


def Q1_view(req: WSGIRequest):
    if req.method == 'POST':
        form = Q1_form(req.POST)
        if form.is_valid():
            manufact = form.cleaned_data['manufact']
            mod_name = form.cleaned_data['mod_name']
            return render(req, 'Q1_res.html', {
                'manufact': manufact,
                'mod_name': mod_name
            })
    else:
        form = Q1_form()

    return render(req, 'Q1.html', {'form': form})

def Q1_res_view(req: WSGIRequest):
    return render(req, 'Q1_res.html')


def Q2_view(req: WSGIRequest):
    form = Q2_form()
    if req.method == 'POST':
        form = Q2_form(req.POST)
        if form.is_valid():
            req.session['name'] = form.cleaned_data['name']
            req.session['roll'] = form.cleaned_data['roll']
            req.session['subject'] = form.cleaned_data['subject']
            return redirect('Q2_sec')
        
    return render(req, 'Q2.html', {'form': form})

def Q2_sec_view(req: WSGIRequest):
    name = req.session.get('name', '')
    roll = req.session.get('roll', '')
    subject = req.session.get('subject', '')
    
    return render(req, 'Q2_sec.html', {
        'name': name,
        'roll': roll,
        'subject': subject
    })

def A1_view(req: WSGIRequest):
    form = A1_form()
    selected_items = []

    if req.method == 'POST':
        form = A1_form(req.POST)
        if form.is_valid():
            selected_items = []
            if form.cleaned_data['wheat']:
                selected_items.append(('Wheat', 40))
            if form.cleaned_data['jaggery']:
                selected_items.append(('Jaggery', 60))
            if form.cleaned_data['dal']:
                selected_items.append(('Dal', 80))
    
    return render(req, 'A1.html', {
        'form': form,
        'selected_items': selected_items
    })