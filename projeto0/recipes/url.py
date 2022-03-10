from django.urls import path
from recipes.views import sobre, home

urlpatterns = [
    path('sobre/', sobre),
    path('', home)
]