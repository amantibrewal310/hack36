from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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
