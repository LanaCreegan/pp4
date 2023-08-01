from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe

class Recipe(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created_on')
    template_name = 'recipes.html'
    paginate_by = 6

class RecipeDetail(View):

     def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-date_created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipes_detail.html",
            {
                "post": recipe,
                "comments": comments,
                "liked": liked
            },
        )