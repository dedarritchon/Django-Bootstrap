from django.contrib import messages
# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate

# Register
from users.forms import CustomUserCreationForm
from users.controllers import UserController

# Logout
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # Admin Page
            return render(request, "home/admin.html",
                          {'current_user': request.user})
        # Normal User Home Page
        return render(request, "home/user.html",
                      {'current_user': request.user})
    return redirect('/login')


def register(request):
    # Custom user creation form
    form = CustomUserCreationForm()
    return render(request, "register.html", {'form': form})


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                messages.success(request, "You are logged in")
                return redirect('/')
        messages.error(request, "Failed to Log in")

    return render(request, "login.html", {'form': form})


def logout(request):
    do_logout(request)
    messages.success(request, "You are logged out")
    return redirect('/')


def about(request):
    messages.warning(request, "Testing a warning message")
    return redirect('/')


def pricing(request):
    return render(request, "pricing.html")
