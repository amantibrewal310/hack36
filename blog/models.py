from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    #date_posted = models.DateTimeField(auto_now=True)
    #date_posted = models.DateTimeField(auto_now_add=True)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes_total = models.IntegerField(default=0)

    #image field added 
    image = models.ImageField(upload_to = 'images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.pk})


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    pp = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.content



# class added for disallowing multiple upvotes by same user

class Vote(models.Model):
    postID = models.ForeignKey(Post,on_delete=models.CASCADE)
    userID = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)