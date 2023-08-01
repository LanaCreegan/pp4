from django.contrib import admin
from recipes.models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
        
        summernote_fields = ('description')
