from django.shortcuts import render
from .models import databook
import random
from algo.tfdif import * 
from algo.ditto_text import *
# Create your views here.


def home_view(request):
	return render(request, "Mainpage.html", {"error": ""})



def result_view(requests, mid):
	if requests.POST:
		if len(s:=requests.POST['text'])  > 25:
			l = {}
			for i in databook.objects.all():
				score = round(list(check_plagiarism(s, i.input_text)).pop()[2] * 100, 2)
				l[score] = [i.input_text, i.date, i.time]

			finale = l[max(l.keys())]
			obj = concordance_reporter(fn1=s, fn2=finale[0])
			s = """"""
			for o in obj:
				s += o
				s += "\n\n"

			dumb_data = {
				"simm": max(l.keys()),
				"text": s,
				"date": finale.pop(),
				"time": finale.pop(),
				}
			return render(requests, "Results.html", dumb_data)
		else:
			return render(requests, "Mainpage.html", {"error": "* string too small to Compare please provide text more than 25 words"})