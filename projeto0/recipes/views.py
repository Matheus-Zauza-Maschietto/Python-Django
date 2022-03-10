from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', status=200, context={'nome': 'Matheus Zauza Maschietto'})

def sobre(request):
    return HttpResponse('Sobre')

