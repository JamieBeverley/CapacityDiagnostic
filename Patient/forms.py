from django import forms
from models import Questions, Profile
# class ParticipantForm(forms.Form):
# 	years = [x for x in range(1920,2018)]
# 	dateOfBirth = forms.DateField(widget=forms.SelectDateWidget(years=years))

class QuestionForm(forms.ModelForm):
    """For creating Question forms"""
    class Meta:
        model = Questions
        fields = ['Q1',"Q2","Q3","Q4","Q5","Q6","Q7","Q8"]
        widgets={}
        for i in fields:
            widgets[i] = forms.RadioSelect()
        widgets["Q8"] = forms.Textarea()


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['healthcardNumber','isResearcher']
		widgets = {'healthcardNumber': forms.TextInput}