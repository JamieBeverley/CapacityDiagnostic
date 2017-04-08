from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import (render, redirect, get_object_or_404)
from django.template import loader
from django.contrib.auth.decorators import login_required
from Patient.models import Profile
from Patient.forms import ProfileForm
from Researcher.views import *

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

def about(request):
        template = loader.get_template('./about.html')
        return HttpResponse(template.render({},request))


def researcher_login(request):
	template = loader.get_template('./researcher_login.html')
	errorMsg=''
	form = AuthenticationForm()

	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = User.objects.get(username = request.POST['username'])
			profile = Profile.objects.get(user_id=user)
			if profile.isResearcher:
				user = authenticate(username=request.POST['username'],password=request.POST['password'])
				if user is not None:
					return redirect('/researcher_home')
				else:
					errorMsg = 'Error - please double check your password/username!'
			else:
				errorMsg=errorMsg+"Sorry, you must be a researcher. "
		else:
			errorMsg = errorMsg + 'validation error'
	return HttpResponse(template.render({'errorMsg':errorMsg,'form':form},request))

def new_account(request):
	errorMsg = ""
	if request.method == 'POST':
		# username = request.POST['username']
		# password = request.POST['password']
		uForm = UserCreationForm(request.POST)
		pForm = ProfileForm(request.POST)
		if pForm.is_valid() and uForm.is_valid():
			user = uForm.save() #User.objects.create_user(username=username,password=password)
			# user.save()
			# if (reques)
			profile = Profile.objects.create(user=user,isResearcher=(request.POST['isResearcher']=='on'),healthcardNumber=pForm.cleaned_data['healthcardNumber'])
			profile.save()
			researcher_home(request)
			# return redirect('/login')
		else:
			return HttpResponse("pForm not validated")
			errorMsg =  "Form validation error"
	userForm = UserCreationForm()
	profileForm = ProfileForm()
	template = loader.get_template('./new_account.html')
	context = {'userForm':userForm,'profileForm':profileForm, 'errorMsg':errorMsg, 'errLen':(len(errorMsg))}
	return HttpResponse(template.render(context,request))
