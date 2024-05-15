from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "homepage/index.html")


def posts(request):
    return render(request, "homepage/posts.html")


def blog(request):
    return render(request, "homepage/blog.html")
