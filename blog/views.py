from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    return render(request, "contact.html")

def post_detail(request, post_id):
    return HttpResponse(f"Post ID: {post_id}")

def blog_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return render(request, 'success.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
