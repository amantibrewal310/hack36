from django.shortcuts import render

def home(request):
	return render(request,'hack/home.html')



def about(request):
	return render(request,'hack/about.html')