from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipes_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipes_like'),
    path('add_recipe', views.RecipeAdd.as_view(), name='recipe_add'),
    path('edit_recipe/<int:pk>', views.RecipeEdit.as_view(), name='recipe_edit'),
]

