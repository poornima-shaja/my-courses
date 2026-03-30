from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("category/<str:listing_category>", views.category, name="category"),
    path("all_categories",views.all_categories, name="all_categories"),
    path("watchlist_add/<int:listing_id>", views.watchlist_add, name="watchlist_add"),
    path("watchlist_remove/<int:listing_id>", views.watchlist_remove, name="watchlist_remove"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("owner_user/<int:listing_id>", views.owner_user, name="owner_user"),
    path("comments/<int:listing_id>", views.comments, name="comments"),

]
