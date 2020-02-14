from django.shortcuts import render


def home(request):
    return render(request, 'hack/base.html')

def fblogin(request):
    return render(request, 'hack/fblogin.html')