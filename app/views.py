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

users = [
	{
		'name': 'Dima'
	},
	{
		'name': 'Timur'
	},
	{
		'name': 'Alex'
	},
	{
		'name': 'Mor'
	},
	{
		'name': 'Elad'
	},
]

def home(request):
	context = {
		'posts': posts,
		'users': users
	}
	return render(request, 'home/home.html', context)

def about(request):
	return render(request, 'about/about.html')

