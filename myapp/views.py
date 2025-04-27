from django.shortcuts import render

def home(request):
    context = {'nombre': 'David'}  
    return render(request, 'myapp/home.html', context)
