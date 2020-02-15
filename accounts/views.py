from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import RegistrationForm, EditProfileForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    return render(request,'accounts/login.html')

# social login cancelled
def login_cancelled(request):
    return render(request, 'accounts/login.html')

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

def sign_in_view(request):
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

@login_required(login_url="/accounts/sign_in")
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



# user porfoilio as viewed by others, for every user

def portfolio(request):
    return render(request, 'accounts/portfolio.html')

@login_required(login_url="/accounts/sign_in")
def edit_portfolio(request):
    if request.method=="POST":
        userprofile = UserProfile()
        userprofile.user = request.user
        
        # userprofile.first_name = request.POST['first_name']
        # userprofile.last_name = request.POST['last_name']
        userprofile.bio = request.POST['bio']
        userprofile.address = request.POST['address']
        userprofile.city = request.POST['city']
        if request.POST['website'].startswith('http://') or request.POST['website'].startswith('https://'):
            userprofile.website = request.POST['url']
        else :
            userprofile.website = 'http://' + request.POST['website']
        print(request.POST['skills'])
        userprofile.phone = request.POST['phone']
        userprofile.skills = request.POST['skills']
        userprofile.image = request.FILES['image']
        print(userprofile.user_id)
        userprofile.save()

        return redirect('/')
    else:
        return render(request,'accounts/update_portfolio.html')
