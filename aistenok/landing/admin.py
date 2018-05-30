from django.contrib import admin
from .models import *

class SubscriberAdmin (admin. ModelAdmin):
	# list display = ['name', 'email']
	list_display = [field.name for field in Subscriber._meta.fields]  # field.name for field in Subscriber._meta.fields достает имена полей из всех полей, чтобы не перечислять все
														  			  # Subscriber._meta.fields достает все поля
	list_filter = ['name', 'surname', 'login']
	search_fields = ['login', 'name', 'surname', 'tel']
	# inlines = [FieldMappingInline]														  
	# fields = [] # перечисление полей
	# exclude = ['type'] # исключение полей
	# list_filter = ('report_data',) # в админке появляется фильтр, где можно отфильтровать по полям
	# search_fields = ['category', 'subCategory', 'suggestKeyword'] # появляется поиск по имени поля

	class Meta:
		model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin) #регистрируем в админке нашу модель