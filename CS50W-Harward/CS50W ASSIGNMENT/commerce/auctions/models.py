from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image = models.URLField(max_length=200, blank=True)
    amount = models.DecimalField( max_digits=10, decimal_places=2)
    category = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_listings")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist_listings")

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_listings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_listings")
    bid_amount = models.DecimalField( max_digits=10, decimal_places=2)

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=500)
    timestamp  = models.DateTimeField(auto_now_add=True)

