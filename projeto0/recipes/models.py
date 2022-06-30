from distutils.command.upload import upload
from pyexpat import model
from django.db import models


class Recipe(models.Model):
    tittle = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.SmallIntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.SmallIntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.DateTimeField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')

# Create your models here.
