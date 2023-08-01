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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_created_on', 'approved')
    list_filter = ('approved', 'date_created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)