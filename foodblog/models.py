from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_blog")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    favourites = models.ManyToManyField(User, related_name="recipe_favourites")


class Meta: 
    ordering = ['date_created_on']


def __str__(self):
    return self.title
