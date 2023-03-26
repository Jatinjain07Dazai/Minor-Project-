from django.shortcuts import render
from .models import databook
# Create your views here.


def home_view(requests, *args, **kwargs):
	return render(requests, "Mainpage.html", {})



def result_view(requests, *args, **kwargs):
	return render(requests, "Basem.html", {})