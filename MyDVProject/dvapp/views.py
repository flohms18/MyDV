from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator

from . models import Article,Category, GlossaryTerm

# Create your views here.

def index(request):
    obj = Article.objects.all().order_by('-published_at')    
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {
        'obj': obj,
        'page_obj' : page_obj,
    })

def about(request):
    return render(request,'about.html')


def glossary(request):
    glossary_dict = {}
    terms = GlossaryTerm.objects.all().order_by("term")
    for term in terms:
        FirstLetter = term.term[0].upper()
        if FirstLetter not in glossary_dict:
            glossary_dict[FirstLetter] = []
        glossary_dict[FirstLetter].append(term)

    return render(request, 'glossary.html', {
        'glossary_dict': glossary_dict})

def about(request):
    return render(request, 'about.html')

def category(request):
    categories = Category.objects.all()  
    return render(request, "category.html", {
        'categories': categories
    })


def category_articles(request,category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category).order_by('published_at')
    return render(request,'index.html', {
        'category' : category,
        'articles' : articles
    })

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)    
    return render(request, "/article_detail.html", {
        'article': article
})