from django.http import HttpResponse

def blog_index(request):
    return HttpResponse("Blog main page")

def post_detail(request, post_id):
    return HttpResponse(f"Post ID: {post_id}")
