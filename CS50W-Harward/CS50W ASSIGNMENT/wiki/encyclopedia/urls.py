from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("random", views.random_page, name="random_page"),
    path("new", views.new, name="new"),
    path("edit/<str:title>", views.edit, name="edit"),


]
