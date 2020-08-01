from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from users.models import EmployeeProfile
from users.forms import EmployeeProfileUpdateForm
# Create your views here.

@login_required
def update_profile(request):
    profile = request.user.employeeprofile
    if request.method == 'POST':

        form = EmployeeProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            if data['picture']:
                profile.picture = data['picture']
            if data['resume']:
                profile.resume = data['resume']

            profile.save()
            return  redirect('profile')
    else:
        form = EmployeeProfileUpdateForm()
        print('not works')


    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form,
        }
    )

def login_view(request):
    logout(request)
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'users/login.html', {'error':'Invalid username or password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            password_confirmation = request.POST['password_confirmation']
            if password != password_confirmation:
                return render(request,'users/register.html',{'error':'Confirmation password does not match'})

            user = User.objects.create_user(username=username, password=password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

            profile = EmployeeProfile(user=user)
            profile.save()

            return redirect('login')

    except IntegrityError:
        return render(request,'users/register.html',{'error':'This user already exist, try with other'})

    return render(request, 'users/register.html', { 'profile' : profile })

@login_required
def home(request):
    profile = request.user.employeeprofile
    return render(request, 'users/home.html', { 'profile' : profile })

@login_required
def profile(request):
    profile = request.user.employeeprofile
    print(profile)
    return render(request, 'users/profile.html', { 'profile' : profile })

@login_required
def settings(request):
    profile = request.user.employeeprofile
    return render(request, 'users/settings.html', { 'profile' : profile })

@login_required
def notifications(request):
    profile = request.user.employeeprofile
    return render(request, 'users/notifications.html', { 'profile' : profile })
