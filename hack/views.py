from django.shortcuts import render


def home(request):
<<<<<<< HEAD
    return render(request, 'hack/index.html')
=======
    return render(request, 'hack/base.html')

def fblogin(request):
    return render(request, 'hack/fblogin.html')
>>>>>>> 31ed846389ab310cff8d6bfff88716452e1ec105
