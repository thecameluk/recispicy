from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html')

def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
def contact(request):
    return HttpResponse('Hello Contact')

def about(request):
    return HttpResponse('Hello About')