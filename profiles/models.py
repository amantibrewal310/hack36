from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Skills(models.Model):
	title = models.CharField(max_length = 30)
	description = models.TextField()


	def __str__(self):
		return self.title

class Profiles(models.Model):
	# profile_id = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 30)
	image= models.ImageField(upload_to='events/',blank=True, null=True)
	address=models.CharField(max_length=80,blank=True,null=True)
	phone=models.CharField(max_length=10,blank=True,null=True)
	email=models.CharField(max_length=50,blank=True,null=True)
	skills = models.ManyToManyField(Skills)
	bio=models.TextField()


	def __str__(self):
		return self.name



	
