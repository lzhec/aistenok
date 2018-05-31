from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product

def landing(request):
	products = Product.objects.filter(is_active=True) # выводим активные товары на страницу
	form = SubscriberForm(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		new_form = form.save() #сохраняем переданную форму в админке (появляется новый подписчик)

	return render(request, 'landing/index.html', locals())