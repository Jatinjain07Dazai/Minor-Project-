from django.db import models

# Create your models here.

class databook(models.Model):
	input_text = models.TextField()
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)

	