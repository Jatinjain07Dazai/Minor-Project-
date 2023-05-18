from django.shortcuts import render, redirect
from .models import databook, fackey, stukey
import random
from algo.tfdif import * 
from algo.ditto_text import *
# Create your views here.

def home_view(request):	
	return render(request, "Mainpage.html", {"error": ""})

def role_v(request):
	return render(request, "Rolepick.html", {})


def fmenu_v(request):
	return render(request, "fachoice.html", {})


def add(request, *args, **kwargs):
	con = {}
	if request.POST:
		if len(txt:=request.POST.get('text', 'Null')) > 25:
			databook.objects.create(input_text=txt, Author=request.POST.get('Author', 'Null'), Subject=request.POST.get('subject', 'Null'))
			con={'msg': "* The record has been added in database."}
		else:
			con ={'msg': "* The record is too short or invalid to be stored"}

	return render(request, "addnew.html", con)



def login_f(request):
	name='testfac'
	password = '123456789'
	con = {"error": ""}
	if request.POST:
		if request.POST.get("fid", "Null") == name and request.POST.get("pas", "Null") == password:
			return render(request, "fachoice.html", {})
		else:
			con = {"error": "* username and password is incorrect.Please enter correct Password.."}
	return render(request, "faculty.html", con)

def login_u(request):
	name='jatin'
	password = 'blastoff'
	con = {"error": ""}
	if request.POST:
		if request.POST.get("uid", "Null") == name and request.POST.get("pas", "Null") == password:
			return render(request, "mainpage.html", {})
		else:
			con = {"error": "* username and password is incorrect.Please enter correct Password.."}
	return render(request, "student.html", con)


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
