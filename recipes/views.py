from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Recipe

class Recipe(ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created_on')
    template_name = 'recipes.html'
    paginate_by = 4