from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import (render, redirect, get_object_or_404)
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse

def index(request):
	# if (request.user.is_athenticated()):
		# return HttpResponse("logged in")
	return redirect("/login")


@login_required
def logout_user(request):
	logout(request)
	# return HttpResponse("asdf")
	return redirect('../login')

# def newAccount(request):
	# if (request.method == 'POST'):

def new_account(request):
	errorMsg = ""
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password1']
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=username,password=password)
			user.save()
			return redirect('/login')
		else:
			errorMsg =  "Form validation error"
	form = UserCreationForm()
	template = loader.get_template('./new_account.html')
	context = {'form':form, 'errorMsg':errorMsg, 'errLen':(len(errorMsg))}
	return HttpResponse(template.render(context,request))