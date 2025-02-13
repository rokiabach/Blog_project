from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def post(request):
    return render(request, 'post.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def connexion(request):
    return render(request, 'connexion.html', {})

def inscription(request):
    return render(request, 'inscription.html', {})