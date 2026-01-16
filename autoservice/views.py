from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("INDEX page")


def bio(request, username):
    return HttpResponse(f"Bio page of {username}")

def home(request):
    return HttpResponse("HOME page")

def article_detail(request, id):
    return HttpResponse(f"Article ID: {id}")

def basic(request):
    context = {
        'title': 'My Blog',
        'posts_count': 5,
        "posts": ['First post', 'Second post', 'Third post', "Forrek post", "Fifftyysent post" ]
    }
    return render(request, 'basic/index.html', context)
