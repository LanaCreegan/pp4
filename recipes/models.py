from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    date_created_on = models.DateTimeField(auto_now_add=True)
    date_updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500, null=True)
    featured_image = CloudinaryField('image', default='placeholder')


    class Meta:
        ordering = ['date_created_on']

    def __str__(self):
        return str(self.title)