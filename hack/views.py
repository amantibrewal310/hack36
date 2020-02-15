from django.shortcuts import render


def home(request):
    return render(request, 'hack/index.html')
def home1(request):
    return render(request, 'hack/base1.html')
