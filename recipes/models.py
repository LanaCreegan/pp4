import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_post')
    date_updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    overview = models.TextField(blank=True)
    date_created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="recipe_likes", blank=True)

    class Meta:
        ordering = ['-date_created_on']

    def __str__(self):
        return str(self.title)

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date_created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

