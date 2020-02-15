from django.db import models

class Survey(models.Model):
	name=models.CharField(max_length=80)
	skills=models.CharField(max_length=80)
	city=models.CharField(max_length=80)
	age=models.IntegerField()
	edc_background=models.TextField()