from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="home"),
    path("posts", views.posts, name="posts"),
    path("blog", views.blog, name="blog"),
    path("post", views.post, name="post"),
    path("admin_login", views.admin_login, name="admin_login"),
    path("admin_logout", views.admin_logout, name="admin_logout"),
    path("create_post", views.create_post, name="create_post"),
    path("about", views.about, name="about"),
    path("success", views.success, name="success"),

]
