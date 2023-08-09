from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-date_created_on")
    template_name = 'recipes.html'
    paginate_by = 6

class RecipeDetail(View):

     def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-date_created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipes_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

        def post(self, request, slug, *args, **kwargs):

            queryset = Recipe.objects.filter(status=1)
            recipe = get_object_or_404(queryset, slug=slug)
            comments = post.comments.filter(approved=True).order_by("-date_created_on")
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True

            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.recipe = recipe
                comment.save()
            else:
                comment_form = CommentForm()

            return render(
                request,
                "recipes_detail.html",
                {
                    "recipe": recipe,
                    "comments": comments,
                    "commented": True,
                    "comment_form": comment_form,
                    "liked": liked
                },
            )

    

class RecipeLike(View):
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipes_detail', args=[slug]))



