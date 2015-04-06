from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


######################################################
###### Shows the list of Sale Items

@view_function
def process_request(request):
	params = {}

	SaleItems = hmod.SaleItems.objects.all().order_by('name')
	params['SaleItems'] = SaleItems


	return templater.render_to_response(request, 'saleItem.html', params)

######################################################
###### Edit a Sale Item

@view_function
def edit(request):
	params = {}

	try:
		saleItem = hmod.SaleItems.objects.get(id=request.urlparams[0])
	except hmod.SaleItems.DoesNotExist:
		return HttpResponseRedirect('/homepage/saleItem/')

	form = SaleItemEditForm(initial={
		'name': saleItem.name,
		'description': saleItem.description,
		'lowPrice': saleItem.lowPrice,
		'highPrice': saleItem.highPrice,
	})
	if request.method == 'POST':
		form = SaleItemEditForm(request.POST)
		form.saleItemid = saleItem.id
		if form.is_valid():
			saleItem.name = form.cleaned_data['name']
			saleItem.description = form.cleaned_data['description']
			saleItem.lowPrice = form.cleaned_data['lowPrice']
			saleItem.highPrice = form.cleaned_data['highPrice']
			saleItem.save()
			return HttpResponseRedirect('/homepage/saleItem/')  		




	params['form'] = form
	params['saleItem'] = saleItem
	return templater.render_to_response(request, 'saleItem.edit.html', params)

class SaleItemEditForm(forms.Form):
	name = forms.CharField(required = True, max_length = 100)
	description = forms.CharField(required = True, max_length = 300)
	lowPrice = forms.DecimalField(required = True)
	highPrice = forms.DecimalField(required = True)

#####################################################
########  Create a Sale Item
@view_function
def create(request):
	saleItem = hmod.SaleItems()
	saleItem.name = ''
	saleItem.description = ''
	saleItem.lowPrice = '0.00'
	saleItem.highPrice = '0.00'
	saleItem.save()

	return HttpResponseRedirect('/homepage/saleItem.edit/{}'.format(saleItem.id))

#####################################################
########  Delete a User
@view_function
def delete(request):
	try:
		saleItem = hmod.SaleItems.objects.get(id=request.urlparams[0])
	except hmod.SaleItems.DoesNotExist:
		return HttpResponseRedirect('/homepage/saleItem/')
	
	saleItem.delete()

	return HttpResponseRedirect('/homepage/saleItem/'.format(saleItem.id))









