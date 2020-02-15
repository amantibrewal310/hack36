from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Skills(models.Model):
	title = models.CharField(max_length = 30)
	description = models.TextField()


	def __str__(self):
		return self.title


class UserProfile1(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    bio = models.TextField(default="")
    image = models.ImageField(upload_to='profile/img/',blank=True,null=True)
    address = models.CharField(max_length=80,blank=True,null=True)
    city = models.CharField(max_length=100, default="")
    website = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=0)
    skills = models.TextField(null=True)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    website = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=0)
    friends = models.ManyToManyField("UserProfile", blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return "/accounts/profile/{}".format(self.pk)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to{}".format(self.from_user.username, self.to_user.username)


class Message(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mess_to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mess_from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=200)


    def __str__(self):
        return "From {}, to{}".format(self.from_user.username, self.to_user.username)


class Appoint(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='appoint_to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='appoint_from_user', on_delete=models.CASCADE)
    message = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to{}".format(self.from_user.username, self.to_user.username)

