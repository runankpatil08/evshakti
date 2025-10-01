from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import ElectricTwoWheeler_form
from .models import ElectricTwoWheeler

from .models import Review
from .forms import ReviewForm



def add_review(request):
    reviews = Review.objects.all().order_by("-created_at")

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            # Only assign user if logged in
            if request.user.is_authenticated:
                review.user = request.user
            review.save()
            return redirect("reviews")
    else:
        form = ReviewForm()

    return render(request, "ev_app/reviews.html", {"form": form, "reviews": reviews})

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        review.delete()
        return redirect("reviews")
    return redirect("reviews")


# ------------------------------
# Home Page + Features
# ------------------------------
def home_view(request):
    ev = ElectricTwoWheeler.objects.all()
    return render(request, "ev_app/home.html", {"ev": ev})


def longBatteryLife(request):
    return render(request, "ev_app/longbattery.html")


def fastandsmooth(request):
    return render(request, "ev_app/fastandsmooth.html")


def ecofriendly(request):
    return render(request, "ev_app/ecofriendly.html")


def contact_view(request):
    return render(request, "ev_app/contact.html")


# ------------------------------
# CRUD for ElectricTwoWheeler
# ------------------------------
def add_view(request):
    form = ElectricTwoWheeler_form()
    if request.method == "POST":
        form = ElectricTwoWheeler_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product added successfully.")
            return redirect("show")
    return render(request, "ev_app/add.html", {"form": form})


def show_view(request):
    ev = ElectricTwoWheeler.objects.all()
    return render(request, "ev_app/show.html", {"ev": ev})


def update_view(request, id):
    ev = get_object_or_404(ElectricTwoWheeler, id=id)
    form = ElectricTwoWheeler_form(instance=ev)
    if request.method == "POST":
        form = ElectricTwoWheeler_form(request.POST, request.FILES, instance=ev)
        if form.is_valid():
            form.save()
            messages.info(request, "✏️ Product updated successfully.")
            return redirect("show")
    return render(request, "ev_app/add.html", {"form": form})


def delete_view(request, id):
    ev = get_object_or_404(ElectricTwoWheeler, id=id)
    ev.delete()
    messages.error(request, "🗑️ Product deleted successfully.")
    return redirect("show")
