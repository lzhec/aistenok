from django.contrib import admin
from .models import *

class SubscriberAdmin (admin. ModelAdmin):
	list_display = [field.name for field in Subscriber._meta.fields]
	list_filter = ['name', 'surname', 'login']
	search_fields = ['login', 'name', 'surname', 'tel']

	class Meta:
		model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin) #регистрируем в админке нашу модель