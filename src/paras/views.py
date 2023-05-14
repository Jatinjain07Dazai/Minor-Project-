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
		if len(s:=requests.POST['text']) > 25: 
			l = {}
			for i in databook.objects.all():
				score = round(list(check_plagiarism(s, i.input_text)).pop()[2] * 100, 2)
				l[score] = [i.input_text, i.date, i.time, i.Author, i.Subject]
			print(l.keys())
			finale = l[max(l.keys())]
			obj = concordance_reporter(fn1=s, fn2=finale[0])
			dumb_data = {
			"sub" : finale.pop(),	
			"Aut" : finale.pop(),
			"time": finale.pop(),
			"date": finale.pop(),
			"context":finale.pop(),
			"res" : obj, 
			"simm": max(l.keys()),
			"text": s,
			}
			return render(requests, "Results.html", dumb_data)
	return render(requests, "Mainpage.html", {"error": "text is invalid."})
