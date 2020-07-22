from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            return redirect('reftable')
        else:
            return render(request,'users/login.html', {'ERROR':'Invalid username or password'})

    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def home(request):
    return render(request, 'users/home.html')

def profile(request):
    return render(request, 'users/profile.html')
