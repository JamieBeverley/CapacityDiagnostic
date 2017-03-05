from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import (render, redirect, get_object_or_404)
from django.template import loader
from django.contrib.auth.decorators import login_required
from Patient.models import Profile
from Patient.forms import ProfileForm


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
		uForm = UserCreationForm(request.POST)
		pForm = ProfileForm(request.POST)
		if pForm.is_valid() and pForm.is_valid():
			user = User.objects.create_user(username=username,password=password)
			user.save()
			profile = Profile.objects.create(user=user,healthcardNumber=pForm.cleaned_data['healthcardNumber'])
			profile.save()
			return redirect('/login')
		else:
			return HttpResponse("pForm not validated")
			errorMsg =  "Form validation error"
	userForm = UserCreationForm()
	profileForm = ProfileForm()
	template = loader.get_template('./new_account.html')
	context = {'userForm':userForm,'profileForm':profileForm, 'errorMsg':errorMsg, 'errLen':(len(errorMsg))}
	return HttpResponse(template.render(context,request))

