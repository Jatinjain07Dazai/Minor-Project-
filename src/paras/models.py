from django.db import models

# Create your models here.

class databook(models.Model):
	input_text = models.TextField()
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	Author = models.CharField(max_length=40, default="fac")
	Subject = models.CharField(max_length=80,  default="computer science")
	