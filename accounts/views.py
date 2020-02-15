from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import RegistrationForm, EditProfileForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout
# Create your views here.

def login_view(request):
    return render(request,'accounts/login.html')

def signup_view(request):
    if(request.method=='POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("Please Enter good password")
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'accounts/signup.html',args)

    # return render(request,'accounts/signup.html')

def login_view(request):
    if(request.method=='POST'):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request,user)
            if('next' in request.POST):
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    # it is prefrential to use post method for logout otherwise user will logout directly by url only

    if(request.method=='POST'):
        logout(request)
        return redirect('/')
    else:
        return redirect('/')

def edit_profile(request):
    if(request.method=="POST"):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request,'accounts/edit_profile.html',args)
    # return HttpResponse("edit profile")
