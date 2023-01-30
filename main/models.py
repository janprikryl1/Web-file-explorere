from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to="items/", blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=25)
    photo = models.ImageField(blank=True, upload_to="categories/")
    description = models.TextField(blank=False)
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
