from django.db import models

# Create your models here.

class databook(models.Model):
	input_text = models.TextField()
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	Author = models.CharField(max_length=40, default="Prof. Gaurav Shrivastava")
	Subject = models.CharField(max_length=80,  default="Network Security and Cryptography")
	




class fackey(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=36, unique=True)


class stukey(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=36, unique=True)