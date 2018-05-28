from django.contrib import admin
from .models import *

class SybscriberAdmin (admin. ModelAdmin):

	class Meta:
		model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin) #регистрируем в админке нашу модель