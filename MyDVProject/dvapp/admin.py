from django.contrib import admin
from .models import GlossaryTerm, Article, Category

# Register your models here.

admin.site.register(GlossaryTerm)
admin.site.register(Article)
admin.site.register(Category)