from django.contrib import admin

from .models import Category, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'category')
    search_fields = ('title', 'content')
    list_filter = ('category',)
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
