from django.shortcuts import render

def index(request):
    data = {
        'title' : 'Главная страница',
        'values' : ['Some', "Hello", "123"],
        'obj' : {
            'Car': 'BMW',
            'age' : 18,
            "hooby" : 'football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')