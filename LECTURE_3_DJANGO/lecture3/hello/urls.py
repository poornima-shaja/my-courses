from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("bts", views.bts, name="bts"),
    path("<str:name>", views.greet, name="greet")
]
