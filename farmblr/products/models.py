from django.db import models


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.category)

    class Meta:
        verbose_name_plural = 'Categories'
