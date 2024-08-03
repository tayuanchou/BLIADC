from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    return render(request, "homepage/index.html")


def posts(request):
    return render(request, "homepage/posts.html")


def blog(request):

    latest_posts = Post.objects.all().order_by("-date_posted")
    # this is translated to SQL so don't worry about the performance
    return render(request, "homepage/blog.html", {"latest_posts": latest_posts})


def post(request):
    return render(request, "homepage/post.html")


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'homepage/admin_login')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user'] = user.username
            messages.success(request, 'Successfully logged in.')
            return redirect("blog")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "homepage/admin_login.html")


def admin_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("blog")


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        excerpt = request.POST.get('excerpt')
        content = request.POST.get('content')
        category_name = request.POST.get('category')
        file = request.FILES.get('file')

        if not title or not excerpt or not content or not category_name:
            messages.error(request, 'All fields are required.')
            return render(request, 'homepage/create_post.html')

        category = Category.objects.get(caption=category_name)

        # Save post
        post = Post(
            title=title,
            excerpt=excerpt,
            content=content,
            file=file,
            category=category
        )
        post.save()

        messages.success(request, 'Post created successfully!')
        return redirect('blog')

    categories = Category.objects.all()
    return render(request, "homepage/create_post.html", {'categories': categories})


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


def about(request):
    return render(request, "homepage/about.html")


def success(request):
    return render(request, "homepage/success.html")
