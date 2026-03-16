from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class GlossaryTerm(models.Model):
    term = models.CharField(max_length=100,unique=True)
    definition = models.TextField()

    def __str__(self):
        return self.term

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    slug = models.SlugField(unique=True, blank=True,null=True)

    def __str__(self):
        return self.title

    

    