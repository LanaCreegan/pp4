from django.contrib import admin
from recipes.models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
        list_display = ('title', 'slug', 'status', 'date_created_on')
        search_fields = ['title', 'content']
        list_filter = ('status', 'date_created_on')
        prepopulated_fields = {'slug': ('title',)}
        summernote_fields = ('description')
