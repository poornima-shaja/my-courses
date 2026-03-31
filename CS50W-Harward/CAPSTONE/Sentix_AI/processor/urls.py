from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("analyze/", views.analyze, name="analyze"),
    path("details/<int:result_id>", views.details, name="details"),
    path("summarize/", views.summarize, name="summarize"),
    path("extract_keyword/", views.extract_keyword, name="extract_keyword"),
    path('delete/<int:id>/', views.delete, name='delete'),
]