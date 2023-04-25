from django.shortcuts import render
from .models import databook
import random
# Create your views here.


def home_view(request):
	if request.POST:
		if len(s:=request.POST['text'])  > 25:
			print(s)
			databook.objects.create(input_text = s)
	return render(request, "Mainpage.html", {})



def result_view(requests, mid):
	k = databook.objects.last()
	dumb_data = {
		"simm": random.randint(0, 100),
		"date": k.date,
		"time": k.time,
		"text": k.input_text
		}
	return render(requests, "Results.html", dumb_data)