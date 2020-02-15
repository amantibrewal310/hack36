from django.shortcuts import render
from .models import Profiles


def show(request,profiles_id):  
    profiles=Profiles.objects.get(pk=profiles_id) 
    return render(request,"profiles/show.html",{'profiles':profiles})  
