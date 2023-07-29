from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from .models import Recipe

class Recipe(ListView):
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 4

class RecipeDetail(ListView):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "recipes.html",
            {
                "post": Recipe
            },
        )