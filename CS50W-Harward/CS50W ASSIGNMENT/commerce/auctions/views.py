from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from decimal import Decimal


def index(request):
    listings = Listing.objects.filter(is_active=True)
    return render(request, "auctions/index.html",{
        "listings" : listings,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.POST["image"]
        category = request.POST["category"]
        amount = request.POST["amount"]
        owner = request.user

        listings =Listing(title=title, description=description, image=image, category=category,amount=amount, owner=owner)
        listings.save()
        return redirect("index")

    return render(request, "auctions/create.html")

@login_required
def bid(request, listing_id):
    listing=Listing.objects.get(pk=listing_id)
    current_bid = listing.bid_listings.all()
    highest_bid = current_bid.order_by('-bid_amount').first()
    if request.method == "POST":
        bid_amount = request.POST["place_bid"]

        try:
            bid_amount = Decimal(bid_amount)
        except:
            return render(request, "auctions/bid.html",{
                "listing": listing,
                "error": 'InValid amount entered',
                "success": "Your bid has been updated"
            })
        current_amount = highest_bid.bid_amount if highest_bid else listing.amount
        winner = False
        if not listing.is_active and highest_bid and highest_bid.user == request.user:
            winner = True
            return render(request, "auctions/bid.html", {
                "listing": listing,
                "highest_bid": highest_bid,
                "winner": winner
})
        if bid_amount>current_amount:
            Bid.objects.create(listing=listing, user = request.user, bid_amount=bid_amount)
            listing.amount = bid_amount
            listing.save()
        else:
            return render(request, "auctions/bid.html",{
                "listing": listing,
                "error": 'Bid must be higher than the current price',
                "highest_bid": highest_bid,
                
            })
    return render(request, "auctions/bid.html",{
                "listing": listing,
                "success": "Your bid has been updated"
            }) 

def all_categories(request):
    listings = Listing.objects.values_list('category', flat=True).distinct()
    return render(request, "auctions/category.html", {
        "listings": listings
    })


@login_required
def category(request, listing_category):
    listings = Listing.objects.filter(category=listing_category)
    return render(request, "auctions/index.html", {
        "listings": listings,
    })

@login_required
def watchlist(request):
    listings = request.user.watchlist_listings.all()
    return render(request, "auctions/index.html", {
        "listings": listings,
    })

@login_required
def watchlist_add(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.add(request.user)
    return redirect("index")

@login_required
def watchlist_remove(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.remove(request.user)
    return redirect("index")

@login_required
def owner_user(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if listing.owner == request.user:
        listing.is_active = False
        listing.save()
        return render(request,"auctions/index.html",{
        "message":"Auction is closed"
        })
    else:
        return HttpResponse("You are not the user")
    
@login_required
def comments(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == "POST":
        comment_owner = request.user
        content = request.POST["content"]
        Comment.objects.create(user=comment_owner, content=content, listing=listing)
        return redirect("comments" ,listing_id=listing.id)
    comments = Comment.objects.filter(listing=listing)
    return render(request,"auctions/comments.html",{
        "listing":listing,
        "comments":comments
    })