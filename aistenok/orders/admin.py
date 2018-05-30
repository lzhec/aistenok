from django.contrib import admin
from .models import *

# модели админки: заказы

class ProductInOrderInline (admin.TabularInline):
	model = ProductInOrder



class OrderStatusAdmin (admin.ModelAdmin):
	list_display = [field.name for field in OrderStatus._meta.fields]
	list_filter = ['name', 'is_active', 'created']
	
	class Meta:
		model = OrderStatus

admin.site.register(OrderStatus, OrderStatusAdmin)



class ShippingStatusAdmin (admin.ModelAdmin):
	list_display = [field.name for field in ShippingStatus._meta.fields]
	list_filter = ['name', 'is_active', 'created']
	
	class Meta:
		model = ShippingStatus

admin.site.register(ShippingStatus, ShippingStatusAdmin)



class OrderAdmin (admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]
	list_filter = ['customer_name', 'customer_phone', 'order_status', 'shipping_status', 'created']
	search_fields = ['customer_name', 'customer_phone', 'comments', 'created']
	inlines = [ProductInOrderInline]

	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)



class ProductInOrderAdmin (admin.ModelAdmin):
	list_display = [field.name for field in ProductInOrder._meta.fields]
	list_filter = ['order', 'product', 'is_active', 'created']
	search_fields = ['order', 'product', 'created']

	class Meta:
		model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)




