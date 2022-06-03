from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', status=200, context={'recipes': [make_recipe() for _ in range(10)]})


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={'recipe': make_recipe()})
