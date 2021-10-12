import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


def get_unique_path(_, filename):
    """create a unique path for the file to be uploaded"""
    extension = filename.split('.', 1)[-1]
    filename = "{}.{}".format(uuid4(), extension)
    return os.path.join('blog', filename)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    summary = models.TextField(max_length=250)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cover_image = models.ImageField(upload_to=get_unique_path, blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}'. format(self.title)