from django.urls import path
from . import views

urlpatterns = [
    path('', views.Recipe.as_view(), name='recipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]