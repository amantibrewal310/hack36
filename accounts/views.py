from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import RegistrationForm, EditProfileForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

User = get_user_model()

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



#FRIEND REQUEST FUNCTIONS
@login_required
def users_list(request):
    users = UserProfile.objects.exclude(user=request.user)
    print(len(users))
    context = {
        'users': users
    }
    return render(request, "accounts/all_user.html", context)


def send_friend_request(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        frequest, created = FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=user
        )
        users = UserProfile.objects.exclude(user=request.user)
        print(len(users))
        context = {
            'users': users
        }
        return render(request, "accounts/all_user.html", context)


def send_message(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        frequest, created = Message.objects.get_or_create(
            from_user=request.user,
            to_user=user
        )
        frequest.message = request.POST['mess']
        frequest.timestamp = timezone.datetime.now()
        frequest.save()
        users = UserProfile.objects.exclude(user=request.user)
        print(len(users))
        context = {
            'users': users
        }
        return render(request, "accounts/all_user.html", context)


def cancel_friend_request(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404()
        frequest = FriendRequest.objects.filter(
            from_user=request.user,
            to_user=user).first()
        frequest.delete()
        users = UserProfile.objects.exclude(user=request.user)
        print(len(users))
        context = {
            'users': users
        }
        return render(request, "accounts/all_user.html", context)


def cancel_message(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404()
        frequest = Message.objects.filter(
            from_user=request.user,
            to_user=user).first()
        frequest.delete()
        users = UserProfile.objects.exclude(user=request.user)
        print(len(users))
        context = {
            'users': users
        }
        return render(request, "accounts/all_user.html", context)


def accept_friend_request(request, id):
    from_user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    user1 = frequest.to_user
    user2 = from_user
    user1.userprofile.friends.add(user2.userprofile)
    user2.userprofile.friends.add(user1.userprofile)
    frequest.delete()
    users = UserProfile.objects.exclude(user=request.user)
    print(len(users))
    context = {
        'users': users
    }
    return render(request, "accounts/all_user.html", context)

def accept_message(request, id):
    from_user = get_object_or_404(User, id=id)
    frequest = Message.objects.filter(from_user=from_user, to_user=request.user).first()
    user1 = frequest.to_user
    user2 = from_user
    appointment = Appoint()
    appointment.to_user = user1
    appointment.from_user = user2
    appointment.timestamp = timezone.datetime.now()
    appointment.message = frequest.message
    appointment.save()
    frequest.delete()
    users = UserProfile.objects.exclude(user=request.user)
    print(len(users))
    context = {
        'users': users
    }
    return render(request, "accounts/all_user.html", context)


def delete_request(request, id):
    from_user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    frequest.delete()
    users = UserProfile.objects.exclude(user=request.user)
    print(len(users))
    context = {
        'users': users
    }
    return render(request, "accounts/all_user.html", context)


def delete_message(request, id):
    from_user = get_object_or_404(User, id=id)
    frequest = Message.objects.filter(from_user=from_user, to_user=request.user).first()
    frequest.delete()
    users = UserProfile.objects.exclude(user=request.user)
    print(len(users))
    context = {
        'users': users
    }
    users = UserProfile.objects.exclude(user=request.user)
    print(len(users))
    context = {
        'users': users
    }
    return render(request, "accounts/all_user.html", context)


def profile_view(request, pk):
    p = UserProfile.objects.filter(pk=pk).first()
    u = p.user
    sent_request = FriendRequest.objects.filter(from_user=p.user)
    rec_request = FriendRequest.objects.filter(to_user=p.user)
    sent_appoint = Message.objects.filter(from_user=p.user)
    rec_appoint = Message.objects.filter(to_user=p.user)
    button_status ='none'
    friends = p.friends.all()
    print(len(friends))
    if p not in request.user.userprofile.friends.all():
        button_status = 'not_friend'
        if len(FriendRequest.objects.filter(from_user=request.user).filter(to_user=p.user)) == 1:
            button_status = 'friend_request_sent'
    context = {
        'u': u,
        'button_status': button_status,
        'friend_list': friends,
        'sent_friend_requests': sent_request,
        'rec_friend_requests': rec_request,
        'sent_appoint': sent_appoint,
        'rec_appoint': rec_appoint
    }
    return render(request, 'accounts/profile.html', context)