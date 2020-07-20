from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def home(request):
    return render(request, 'users/home.html')

def profile(request):
    return render(request, 'users/profile.html')
