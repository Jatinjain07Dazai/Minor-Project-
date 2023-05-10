from django.shortcuts import render, redirect
from .models import databook
import random
from algo.tfdif import * 
from algo.ditto_text import *
# Create your views here.


def home_view(request):
	return render(request, "Mainpage.html", {"error": ""})



def result_view(requests):
	if requests.POST:
		if len(s:=requests.POST['text'])  > 25:
			l = {}
			for i in databook.objects.all():
				score = round(list(check_plagiarism(s, i.input_text)).pop()[2] * 100, 2)
				l[score] = [i.input_text, i.date, i.time]

			finale = l[max(l.keys())]
			obj = concordance_reporter(fn1=s, fn2=finale[0])
			u = """"""
			for o in obj:
				u += o
				u += "\n"

			dumb_data = {
				"res" : u, 
				"simm": max(l.keys()),
				"text": s,
				"date": finale.pop(),
				"time": finale.pop(),
				}
			return render(requests, "Results.html", dumb_data)
		else:
			return render(requests, "Mainpage.html", {"error": "The Text is not of adequate length to be proccessed for Plagiarism Check."})