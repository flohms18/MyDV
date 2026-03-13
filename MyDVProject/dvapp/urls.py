from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("glossary/",views.glossary, name="glossary")
]