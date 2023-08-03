from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
     'title': 'First post',
     'body': 'first body',
     'author': 'aannoo',
     'date': '3/8/2023'
     },
     {
     'title': 'Second post',
     'body': 'second body',
     'author': 'Rana',
     'date': '6/8/2023'
     }
]
# Create your views here.

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
