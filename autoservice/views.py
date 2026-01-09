from django.http import HttpResponse

def index(request):
    return HttpResponse("INDEX page")


def bio(request, username):
    return HttpResponse(f"Bio page of {username}")

def home(request):
    return HttpResponse("HOME page")

def article_detail(request, id):
    return HttpResponse(f"Article ID: {id}")