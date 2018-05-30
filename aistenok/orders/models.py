from django.db import models
from products.models import Product
from django.db.models.signals import post_save

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
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # total price of all products in order
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
	product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # nmb*product.price
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.product.name

	class Meta:
		verbose_name = 'Товар в заказе'
		verbose_name_plural = 'Товары в заказе'

	# переопределяем метод save для вычисления и сохранения стоимости всех единиц товара
	def save(self, *args, **kwargs):
		product_price = self.product.price
		self.product_price = product_price
		self.total_price = self.nmb * product_price	

		super(ProductInOrder, self).save(*args, **kwargs)



def product_in_order_postsave(sender, instance, created, **kwargs):
	order = instance.order
	all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
	order_total_price = 0
	for item in all_products_in_order:
		order_total_price += item.total_price
	
	instance.order.total_price = order_total_price
	instance.order.save(force_update=True)


post_save.connect(product_in_order_postsave, sender=ProductInOrder)
