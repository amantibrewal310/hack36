from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.signup_view,name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html')),
    path('sign_in/',views.login_view,name='login'),
    path('signout/',views.logout_view,name='logout'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),


]