from django.db import models

class Subscriber (models.Model): #наша модель формы с заданными полями
	email = models.EmailField()
	name = models.CharField(max_length=50)
	real_surname = models.CharField(max_length=50, default='SOME STRING')
	real_name = models.CharField(max_length=50, default='SOME STRING')
	tel = models.CharField(max_length=11, default='SOME DIGITS')

	def __str__(self):
		return '%s %s' % (self.id, self.real_name, self.real_surname)

	class Meta:
		verbose_name = 'MySubscribers'
		verbose_name_plural = 'A lot of Subscribers'