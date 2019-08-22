from django.shortcuts import render, redirect


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def register(request):
    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
