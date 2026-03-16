from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("glossary",views.glossary, name="glossary"),
    path("about", views.about, name="about"),
    path("category", views.category, name="category"),
    path('category/<int:category_id>/', views.category_articles, name='category_posts')
]