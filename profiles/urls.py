
from django.urls import path
from .import views



urlpatterns = [
    path('detail/<int:profiles_id>/',views.show,name='show'),
    
] 