from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Skills(models.Model):
	title = models.CharField(max_length = 30)
	description = models.TextField()


	def __str__(self):
		return self.title

class UserProfile(models.Model):
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

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=User)