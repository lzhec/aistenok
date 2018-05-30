from django.contrib import admin
from .models import *

# модели админки: товары

class ProductImageInline (admin.TabularInline):
	model = ProductImage



class ProductAdmin (admin. ModelAdmin):
	list_display = [field.name for field in Product._meta.fields]
	list_filter = ['name', 'is_active', 'created']
	search_fields = ['name', 'description', 'created']
	inlines = [ProductImageInline]

	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)



class ProductImageAdmin (admin. ModelAdmin):
	list_display = [field.name for field in ProductImage._meta.fields]
	list_filter = ['product', 'is_active', 'created']
	search_fields = ['product', 'created']

	class Meta:
		model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)