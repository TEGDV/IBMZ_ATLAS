from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_view(request):
    logout(request)
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            return redirect('reftable')
        else:
            return render(request,'users/login.html', {'error':'Invalid username or password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    return render(request, 'users/register.html')

@login_required
def home(request):
    return render(request, 'users/home.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')
