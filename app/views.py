from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Dima',
		'title': 'Blog 1',
		'content': 'first post content'
	},
	{
		'author': 'Timur',
		'title': 'Blog 2',
		'content': 'second post content'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'home/home.html', context)

def about(request):
	return render(request, 'about/about.html')

