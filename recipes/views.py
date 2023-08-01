from django.shortcuts import render
from django.views import generic, View
from .models import Recipe

class Recipe(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created_on')
    template_name = 'recipes.html'
    paginate_by = 6

class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(self, slug=slug)

        return render(
            request,
            "recipes.html",
            {
                "post": Recipe
            },
        )