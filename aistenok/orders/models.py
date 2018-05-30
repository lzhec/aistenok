from django.db import models
from products.models import Product

# модели: заказы

class OrderStatus(models.Model):
	name = models.CharField(max_length=24, blank=True, default=None)
	is_active = models.BooleanField(blank=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.name

	class Meta:
		verbose_name = 'Статус заказа'
		verbose_name_plural = 'Статусы заказов'



class ShippingStatus(models.Model):
	name = models.CharField(max_length=24, blank=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.name

	class Meta:
		verbose_name = 'Статус доставки'
		verbose_name_plural = 'Статусы доставок'



class Order(models.Model):
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=None) # total price of all products in order
	customer_name = models.CharField(max_length=128)
	customer_email = models.CharField(max_length=50, blank=True, default=None)
	customer_phone = models.CharField(max_length=30, blank=True, default=None)	
	shipping_address = models.CharField(max_length=128, blank=True, default=None)
	comments = models.TextField(blank=True, default=None)
	order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default=None)
	shipping_status = models.ForeignKey(ShippingStatus, on_delete=models.CASCADE, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return 'Заказ %s' % self.id

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'



class ProductInOrder(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, default=None)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, default=None)
	nmb = models.IntegerField(default=1)
	product_price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=None) # nmb*product.price
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.product.name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
