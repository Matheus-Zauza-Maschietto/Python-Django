from pyexpat import model
from django.db import models


class Recipe(models.Model):
    tittle = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()

# Create your models here.
