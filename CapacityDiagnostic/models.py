from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms


CHOICES1 = (('a','The beach'),('b','An amusement park'),('c','The dinner table'),('d','I am not sure'))
CHOICES2 = (('a',"Vision problems"),('b',"Shortness of breath"),('c',"Headache"),('d',"Pain in her leg"),('e',"I am not sure"))
CHOICES3 = (('a',"reading glasses"),('b',"asthma medication"),('c',"cataract surgery"),('d',"a cast"),('e',"no procedure"),('f',"I am not sure"))
CHOICES4 = (('a',"nausea  and vomitting"),('b',"infection, bleeding, loss of vision, double vision, after-cataract"),('c',"no risk"),('d',"I am not sure"))
CHOICES5 = (('a',"Yes, the minor risks of complications outweighs the risk of the cataract getting worse and requiring a more complicated surgery with more risks later on."),('b',"No, the minor risks of complications does not outweigh the minor risk of the cataract getting worse and requiring a more complicated surgery with more risks later on."),('c',"No, the doctor does not want his patient to receive the surgery"),('d',"I am not sure"))
CHOICES6 = (('a',"Her cataract will heal on its own"), ('b',"Her cataract may get worse"), ('c',"I am not sure"))
CHOICES7 = (('y','Yes',),('n','No'))

class Questions(models.models)
	Q1 = models.CharField(max_length=1,choices=CHOICESAD,verbose_name="Where is the patient at the beginning of the story?")
	Q2 = models.CharField(max_length=1, choices=CHOICESAE,verbose_name="What is the patient's concern?")
	Q3 = models.CharField(max_length=1, choices=CHOICESAF,verbose_name="What does the doctor suggest for the patient?")
	Q4 = models.CharField(max_length=1, choices=CHOICESAD,verbose_name="What are the risks of the surgery that the doctor explains to the patient?")
	Q5 = models.CharField(max_length=1, choices=CHOICESAD,verbose_name="Do the risks of receiving the cataract surgery outweigh the risks of not receiving the surgery?")
	Q6 = models.CharField(max_length=1, choices=CHOICESAC,verbose_name="If the patient does not receive the surgery...")
	Q7 = models.CharField(max_length=1, choices=(('y','Yes'),('n','No')),verbose_name="In your opinion, should the patient receive the surgery?")
	Q8 = models.CharField(max_length=400, verbose_name="Why?")