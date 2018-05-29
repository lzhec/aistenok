from django.db import models
from products.models import Product

class Status(models.Model):
	name = models.CharField(max_length=24, blank=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return 'Статус %s' % self.name

	class Meta:
		verbose_name = 'Статус заказа'
		verbose_name_plural = 'Статусы заказов'



class Order(models.Model):
	customer_name = models.CharField(max_length=128)
	customer_email = models.CharField(max_length=50, blank=True, default=None)
	customer_phone = models.CharField(max_length=30, blank=True, default=None)
	comments = models.TextField(blank=True, default=None)
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return 'Заказ %s %s' % (self.id, self.status.name)

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'



class ProductsInOrder(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, default=None)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.product.name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
