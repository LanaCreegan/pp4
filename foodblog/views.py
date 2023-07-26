from django.shortcuts import render
from django.views import generic
from .models import Recipe

class Recipe(ListView):
    template_name = 'recipes.html'
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.order_by('date_updated_on')

