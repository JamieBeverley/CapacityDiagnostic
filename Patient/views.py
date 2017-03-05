from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import (render, redirect, get_object_or_404)
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import forms

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
	# return HttpResponse("asdf")
	form = forms.QuestionForm()
	return HttpResponse(template.render({'form':form},request))

