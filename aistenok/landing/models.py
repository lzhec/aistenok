from django.db import models

class Subscriber (models.Model): #наша модель формы с заданными полями
	login = models.CharField(max_length=50, default=None)
	pswrd = models.CharField(max_length=50, default=None)
	pswrd_again = models.CharField(max_length=50, default=None)
	email = models.EmailField(max_length=50, default=None)
	surname = models.CharField(max_length=50, default=None)
	name = models.CharField(max_length=50, default=None)
	tel = models.CharField(max_length=12, default=None)
	addr = models.CharField(max_length=256, default=None)
	comment = models.CharField(max_length=512, default=None)

	def __str__(self):
		return '%s %s' % (self.id, self.real_name, self.real_surname)

	class Meta:
		verbose_name = 'MySubscribers'
		verbose_name_plural = 'A lot of Subscribers'