from django.shortcuts import render, get_object_or_404
from django.views import generic 
from .models import Recipe

class RecipePost(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created_on')
    template_name = 'recipes.html'
    paginate_by = 4

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