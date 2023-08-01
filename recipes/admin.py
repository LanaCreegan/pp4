from django.contrib import admin
from recipes.models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

        summernote_fields = ('description')




