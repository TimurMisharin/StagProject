from django.shortcuts import render
from django.http import HttpResponse

# views
def home(request):
    return render(request, 'home/home.html')

def about(request):
	return render(request, 'about/about.html')