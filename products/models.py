from django.db import models
from django.contrib.postgres.fields import ArrayField


class Categories(models.Model):
    name = models.CharField(max_length=64, unique=True)
    image = models.URLField(max_length=256)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    images = ArrayField(models.CharField(max_length=256), blank=True)

    def __str__(self):
        return self.title
    