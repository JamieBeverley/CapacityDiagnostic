from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import (render, redirect, get_object_or_404)
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.
from Patient.models import Profile

from django.http import HttpResponse

def index(request):
	# if (request.user.is_athenticated()):
		# return HttpResponse("logged in")
	return redirect("/home")


# def newAccount(request):
	# if (request.method == 'POST'):
def researcher(request):
	redirect('/home')

@login_required
def researcher_home(request):
	template = loader.get_template('home.html')
	patientScores = Profile.objects.all()
	# return HttpResponse("asdf")
	# hcnum = Profile.objects.get(user_id=request.user).healthcardNumber
	return HttpResponse(template.render({'patientScores':patientScores},request))

