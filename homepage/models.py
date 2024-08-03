from django.db import models
from django.core.validators import MinLengthValidator


class Category(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date_posted = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.FileField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title
