from django.http import Http404, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404

from recipes.models import Recipe


def home(request):
    recipes = get_list_or_404(
        Recipe.objects.filter(is_published=True).order_by('-id'))
    return render(request, 'recipes/pages/home.html', status=200, context={'recipes': recipes})


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True).order_by('-id'))
    return render(request, 'recipes/pages/category.html', status=200, context={'recipes': recipes, 'title': f'{recipes[0].category.name} - Category | '})


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={'recipe': recipe, 'is_detail_page': True, })


def teste(request):
    return render(request, 'recipes/pages/teste.html', status=200, context={'range': range(10), 'atletas': range(2)})
