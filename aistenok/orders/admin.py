from django.contrib import admin
from .models import *


from django.contrib import admin
from .models import *


class StatusAdmin (admin. ModelAdmin):
	list_display = [field.name for field in Status._meta.fields]
	list_filter = ['status', 'is_active', 'created']
	search_fields = ['customer_name', 'customer_phone', 'comments', 'created']

	class Meta:
		model = Status

admin.site.register(Status, StatusAdmin)



class OrderAdmin (admin. ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]
	list_filter = ['status', 'created']
	search_fields = ['customer_name', 'customer_phone', 'comments', 'created']

	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)



class ProductInOrderAdmin (admin. ModelAdmin):
	list_display = [field.name for field in ProductInOrder._meta.fields]
	list_filter = ['order', 'product', 'is_active', 'created']
	search_fields = ['order', 'product', 'created']

	class Meta:
		model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)




