from django.shortcuts import render

# Create your views here.
def Q1_view(req):
    n1 = n2 = op = res = None

    if req.method == 'POST':
        try:
            n1 = float(req.POST.get('n1'))
            n2 = float(req.POST.get('n2'))
            op = str(req.POST.get('op'))

            if op == 'add':
                res = n1 + n2
            elif op == 'sub':
                res = n1 - n2
            elif op == 'mul':
                res = n1 * n2
            elif op == 'div':
                res = n1 / n2
        except (ValueError, TypeError):
            pass

    return render(req, 'Q1.html', {'res': res, 'n1': n1, 'n2': n2})

def Q2_view(req):
    context = {
        'title': 'THE VOGUE',
        'headline': 'The Future of AI',
        'bg_color': '#ffffff',
        'font_color': '#000000',
        'font_size': '60',
        'img_url': ''
    }

    if req.method == 'POST':
        context = {
            'title': req.POST.get('title'),
            'headline': req.POST.get('headline'),
            'bg_color': req.POST.get('bg_color'),
            'font_color': req.POST.get('font_color'),
            'font_size': req.POST.get('font_size'),
            'img_url': req.POST.get('img_url'),
        }

    return render(req, 'Q2.html', context)

def Q3_view(req):
    # The Book Data Dictionary
    book = {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'cover_url': 'https://thecommononline.org/wp-content/uploads/2013/06/Screen-Shot-2017-05-31-at-2.19.46-PM.png',
        'metadata': {'Year': 1925, 'Genre': 'Classic Literature', 'Pages': 180},
        'reviews': ['A masterpiece of the Jazz Age.', 'Beautifully written and tragic.', '5/5 Stars.'],
        'publisher': 'Charles Scribner\'s Sons, New York.'
    }
    
    context = {'book': book}
    return render(req, 'Q3.html', context)

def A1_view(req):
    result = ""
    style = ""
    name = ""
    message = ""

    if req.method == "POST":
        if 'exit' in req.POST:
            return render(req, 'home.html', {'result': "Application Closed (Simulated)"})

        if 'clear' in req.POST:
            return render(req, 'home.html')

        name = req.POST.get('name', '')
        message = req.POST.get('message', '')
        result = f"{name}: {message}"

        if req.POST.get('bold'): style += "font-weight: bold; "
        if req.POST.get('italic'): style += "font-style: italic; "
        if req.POST.get('underline'): style += "text-decoration: underline; "

        color = req.POST.get('color', 'black')
        style += f"color: {color};"

    return render(req, 'A1.html', {
        'result': result, 
        'style': style,
        'name': name,
        'message': message
    })