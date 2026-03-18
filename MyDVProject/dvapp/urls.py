from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("glossary", views.glossary, name="glossary"),
    path("about", views.about, name="about"),
    path("category", views.category, name="category"),
    path("category/<slug:slug>", views.category_detail, name="category_detail"),
    path("article/<slug:slug>", views.article_detail, name="article_detail"),
]