from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('profile/<int:pk>', views.profile_view, name='profile_view'),
    path('request/send/<int:id>/', views.send_friend_request, name='send_friend_request'),
    path('request/cancel/<int:id>', views.cancel_friend_request, name='cancel_friend_request'),
    path('request/accept/<int:id>', views.accept_friend_request, name='accept_friend_request'),
    path('request/delete/<int:id>', views.delete_request, name='delete_request'),
    # ABOVE PATH ARE FOR REQUEST


    path('message/send/<int:id>/', views.send_message, name='send_message'),
    path('message/cancel/<int:id>', views.cancel_message, name='cancel_message'),
    path('message/accept/<int:id>', views.accept_message, name='accept_message'),
    path('message/delete/<int:id>', views.delete_message, name='delete_message'),
    #ABOVE


    path('register/', views.signup_view, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html')),
    path('sign_in/', views.sign_in_view,name='sign_in'),
    path('signout/', views.logout_view,name='logout'),
    path('profile/edit/', views.edit_profile,name='edit_profile'),


]