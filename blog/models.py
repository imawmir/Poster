from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    
    # additional
    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    # author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post_image = models.ImageField(null=True, blank=True, upload_to='posts_images/')
    text = models.TextField()
    post_pic = models.ImageField(null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approve_comment = True
        self.save()
        
    def get_absolute_url(self):
        return reverse("post_detail")
    
        
    def __str__(self):
        self.text