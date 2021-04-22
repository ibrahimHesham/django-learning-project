from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30) 

    def __str__ (self):
        return self.name

class Isbn(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=30, default="def description")
    Isbn = models.UUIDField(default=uuid.uuid4)

    def __str__ (self):
        return self.description

class Books(models.Model):
    title = models.CharField(max_length=30)
    # author = models.CharField(max_length=30)
    price = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Books", default=1)
    categories = models.ManyToManyField(Category)
    Isbn = models.OneToOneField(Isbn, on_delete=models.CASCADE, null=True, blank=True)


    def __str__ (self):
        return self.title

