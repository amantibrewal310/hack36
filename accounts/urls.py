from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),

]