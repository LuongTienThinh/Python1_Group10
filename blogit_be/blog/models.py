from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self) :
        return self.name
    def get_absolute_url(self):
        return reverse('index')

class Post(models.Model):
    title = models.CharField(max_length=264)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=264,default='coding')

    def __str__(self):
        return  f"{self.title} | {self.author.username}"

    def get_absolute_url(self):
        return reverse('index')



