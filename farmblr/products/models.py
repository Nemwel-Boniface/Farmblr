import os
from django.db import models
from uuid import uuid4


def get_unique_path(_, filename):
    """create a unique path for the file to be uploaded"""
    extension = filename.split('.', 1)[-1]
    filename = "{}.{}".format(uuid4(), extension)
    return os.path.join('products', filename)


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=250)
    examples = models.CharField(max_length=250, default=None)

    def __str__(self):
        return '{}'.format(self.category)

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to=get_unique_path)

    def __str__(self):
        return "{}".format(self.product_name)
