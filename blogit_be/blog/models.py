from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
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
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=264,default='coding')
    snippet = models.CharField(max_length=264)
    likes = models.ManyToManyField(User,related_name='blog_posts')
    is_published = models.BooleanField(default=False)
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return  f"{self.title} | {self.author.username}"

    def get_absolute_url(self):
            return reverse('index')
    
    def total_comment(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
     return '%s - %s' % (self.post.title, self.post.author)

