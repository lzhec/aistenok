"""from django import forms
from .models import Subscriber

class SubscriberForm (forms.ModelForm): #создаем форму

	class Meta:
		model = Subscriber #задаем модель формы из models.py 
		exclude = [" "]

