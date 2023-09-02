from django.shortcuts import render, HttpResponse
from . import models

recipes = [
    {
        'author': 'Cliff',
        'title': 'kuku choma',
        'procedure': 'utafunzwa2',
        'date_posted': 'march 3, 2023',
    },
    {
        'author': 'John',
        'title': 'kuku boiro',
        'procedure': 'utafunzwa kabisa',
        'date_posted': 'june 3, 2023',
    }
    ]


# Create your views here.
def home(request):
    # return HttpResponse("Welcome Home")
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html')
