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

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile/")
    website_url = models.CharField(max_length=264,null=True,blank=True)
    github_url = models.CharField(max_length=264,null=True,blank=True)

    def __str__(self):
        return  str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=264)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
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
    
    @classmethod
    def get_posts_with_most_comments_and_likes(cls, limit=5):
        return cls.objects.annotate(num_comments=models.Count('comments'),
                                    num_likes=models.Count('likes')).order_by(-(models.F('num_comments') + models.F('num_likes')))[:limit]

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # Thêm trường user
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return  f"{self.user}"

        

