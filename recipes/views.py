from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe

class Recipe(ListView):
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 4