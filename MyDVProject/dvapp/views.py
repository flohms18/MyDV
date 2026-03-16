from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from . models import Article,Category

# Create your views here.

def index(request):
    return render(request, 'index.html')

def glossary(request):
    return render(request, 'glossary.html')

def about(request):
    return render(request, 'about.html')

def category_posts(request,category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category).order_by('published_at')
    return render(request,'category.html', {
        'category' : category,
        'articles' : articles
    })