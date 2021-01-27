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
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # Admin Page
            return render(request, "home/admin.html",
                          {'current_user': request.user})
        # Normal User Home Page
        return render(request, "home/user.html",
                      {'current_user': request.user})
    # En otro caso redireccionamos al login
    return redirect('/login')


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                messages.success(request, "You are logged in")
                return redirect('/')
        messages.error(request, "Failed to Log in")

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    messages.success(request, "You are logged out")
    return redirect('/')


def about(request):
    messages.warning(request, "Testing a warning message")
    # Redireccionamos a la portada
    return redirect('/')


def pricing(request):
    # Redireccionamos al pricing
    return render(request, "pricing.html")
