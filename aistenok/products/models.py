from django.db import models

# модели: товары

class Product(models.Model):
	name = models.CharField(max_length=128, blank=True, null=True, default=None)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	description = models.TextField(blank=True, null=True, default=None)
	short_description = models.TextField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s, %s' % (self.price, self.name)

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'



class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='products_images')
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.id

	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фото'