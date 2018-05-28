from django.db import models

class Subscribers (models.Model): #наша модель формы с заданными полями
	email = models.EmailField()
	name = models.CharField(max_length=50)
	real_surname = models.CharField(max_length=50, default='SOME STRING')
	real_name = models.CharField(max_length=50, default='SOME STRING')
	tel = models.CharField(max_length=11, default='SOME DIGITS')
