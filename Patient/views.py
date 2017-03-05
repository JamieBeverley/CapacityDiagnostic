from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import (render, redirect, get_object_or_404)
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.
from forms import QuestionForm

from django.http import HttpResponse

def index(request):
	# if (request.user.is_athenticated()):
		# return HttpResponse("logged in")
	return redirect("/home")


# def newAccount(request):
	# if (request.method == 'POST'):

@login_required
def home(request):
	template = loader.get_template('home.html')
	form = QuestionForm()
	if (request.method=="POST"):
		form = QuestionForm(request.POST)
		if form.is_valid():
			score = 0



			for i in [('Q'+str(i)) for i in range(1,7)]:
				score = score+ int(request.POST[i])
			msg = 'Thank you, your score has been recorded'
			return HttpResponse(template.render({'score':score,'form':form,'msg':msg},request))
		else:
			return HttpResponse([(field.label,field.errors) for field in form])
	# return HttpResponse("asdf")
	
	return HttpResponse(template.render({'form':form},request))

