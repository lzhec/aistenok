from django import forms
from .models import Subscribers 

class SubscriberForm (forms.ModelForm): #создаем форму

	class Meta:
		model = Subscribers #задаем модель формы из models.py 
		exclude = [" "]

