from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/',views.signup_view,name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html')),
    path('sign_in/',views.sign_in_view,name='sign_in'),
    path('signout/',views.logout_view,name='logout'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('portfolio/edit',views.edit_portfolio,name='edit_portfolio')

    # temporary portfolio path created
    path('portfolio/', views.portfolio, name='portfolio'),
    # socail login cancelled
    # path('social/login/cancelled/', views.sign_in_view,name='sign_in'),

]