from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="home"),
    path("posts", views.posts, name="posts"),
]
