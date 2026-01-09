from django.http import HttpResponse

def index(request):
    return HttpResponse("INDEX page")


def bio(request, username):
    return HttpResponse(f"Bio page of {username}")
