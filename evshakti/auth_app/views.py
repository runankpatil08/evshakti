from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "✅ Registration successful! Please log in.")

            # Gmail alert
            send_mail(
                subject='Welcome to EVShakti 🚀',
                message=f'Hello {user.username},\n\nThank you for registering at EVShakti!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect("login")
        else:
            messages.error(request, "⚠️ Registration failed. Please check the form.")
    return render(request, "auth_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"👋 Welcome back, {user.username}!")

            # Gmail alert
            send_mail(
                subject='Login Alert 🔑',
                message=f'Hello {user.username},\n\nYou have logged in to your EVShakti account.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect("home")
        else:
            messages.error(request, "❌ Invalid username or password.")
    return render(request, "auth_app/login.html")


def logout_view(request):
    if request.user.is_authenticated:
        email = request.user.email
        username = request.user.username
        logout(request)
        messages.info(request, "🚪 You have been logged out successfully.")

        # Gmail alert
        send_mail(
            subject='Logout Alert 🚪',
            message=f'Hello {username},\n\nYou have successfully logged out from EVShakti.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

    return redirect("login")
