from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


######################################################
###### Shows the list of Products

@view_function
def process_request(request):
	params = {}

	Products = hmod.Products.objects.all().order_by('name')
	params['Products'] = Products


	return templater.render_to_response(request, 'product.html', params)

######################################################
###### Edit an Product

@view_function
def edit(request):
	params = {}

	try:
		product = hmod.Products.objects.get(id=request.urlparams[0])
	except hmod.Products.DoesNotExist:
		return HttpResponseRedirect('/homepage/product/')

	form = ProductEditForm(initial={
		'name': product.name,
		'description': product.description,
		'category': product.category,
		'currentPrice': product.currentPrice,
	})
	if request.method == 'POST':
		form = ProductEditForm(request.POST)
		form.productid = product.id
		if form.is_valid():
			product.name = form.cleaned_data['name']
			product.description = form.cleaned_data['description']
			product.category = form.cleaned_data['category']
			product.currentPrice = form.cleaned_data['currentPrice']
			product.save()
			return HttpResponseRedirect('/homepage/product/')  		




	params['form'] = form
	params['product'] = product
	return templater.render_to_response(request, 'product.edit.html', params)

class ProductEditForm(forms.Form):
	name = forms.CharField(required = True, max_length = 100)
	description = forms.CharField(required = True, max_length = 300)
	category = forms.CharField(required = True, max_length = 30)
	currentPrice = forms.DecimalField(required = True)

#####################################################
########  Create an Product
@view_function
def create(request):
	product = hmod.Products()
	product.name = ''
	product.description = ''
	product.category = ''
	product.currentPrice = '0.00'
	product.save()

	return HttpResponseRedirect('/homepage/product.edit/{}'.format(product.id))

#####################################################
########  Delete a Product
@view_function
def delete(request):
	try:
		product = hmod.Products.objects.get(id=request.urlparams[0])
	except hmod.Products.DoesNotExist:
		return HttpResponseRedirect('/homepage/product/')
	
	product.delete()

	return HttpResponseRedirect('/homepage/product/'.format(product.id))









