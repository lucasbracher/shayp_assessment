from django.contrib.auth.models import User as UserOrig
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    review_score = models.IntegerField()
    genre = models.CharField(max_length=20)

class User(UserOrig):
    books = models.ManyToManyField(Book)