from multiprocessing import context
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfileInfo


# Create your views here.

def reg(request):
    context={}
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'foto_profil' in request.FILES:
                print('found it')
                profile.foto_profil = request.FILES['foto_profil']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'auth/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def log(request):
    context={
        'page_title': 'LOGIN',
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.is_staff == 1:
                return redirect('dashboard_admin')
            elif request.user.is_staff == 0:
                return redirect('beranda')
        else:
            return render(request, 'auth/login.html', context)

    if request.method == "POST":
        
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password=password_login)
        if user is not None:
            login(request, user)
        
        if user is not None:
            auth_login(request, user)
            login(request, user)
            if user.is_staff == 1:
                return redirect('dashboard_admin')
            elif user.is_staff == 0:
                return redirect('beranda')
        else:
            messages.error(request, 'username atau password salah')
            return redirect('/')
    
    return render(request, 'auth/login.html', context)

   
def logout_user(request):
    logout(request)
    return redirect('/')





