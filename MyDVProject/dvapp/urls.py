from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("glossary",views.glossary, name="glossary"),
    path("about", views.about, name="about"),
    path("<int:category_id/",views.category.posts, name='category_posts')
]