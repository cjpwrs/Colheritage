from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


######################################################
###### Shows the list of Items

@view_function
def process_request(request):
	params = {}

	Items = hmod.Items.objects.all().order_by('name')
	params['Items'] = Items


	return templater.render_to_response(request, 'items.html', params)

######################################################
###### Edit an item

@view_function
def edit(request):
	params = {}

	try:
		item = hmod.Items.objects.get(id=request.urlparams[0])
	except hmod.Items.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')

	form = ItemEditForm(initial={
		'name': item.name,
		'description': item.description,
		'value': item.value,
		'standardRentalPrice': item.standardRentalPrice,
	})
	if request.method == 'POST':
		form = ItemEditForm(request.POST)
		form.itemid = item.id
		if form.is_valid():
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.standardRentalPrice = form.cleaned_data['standardRentalPrice']
			item.save()
			return HttpResponseRedirect('/homepage/items/')  		




	params['form'] = form
	params['item'] = item
	return templater.render_to_response(request, 'items.edit.html', params)

class ItemEditForm(forms.Form):
	name = forms.CharField(required = True, max_length = 100)
	description = forms.CharField(required = True, max_length = 300)
	value = forms.DecimalField(required = True)
	standardRentalPrice = forms.DecimalField(required = True)

#####################################################
########  Create an Item
@view_function
def create(request):
	item = hmod.Items()
	item.name = ''
	item.description = ''
	item.value = '0.00'
	item.standardRentalPrice = '0.00'
	item.save()

	return HttpResponseRedirect('/homepage/items.edit/{}'.format(item.id))

#####################################################
########  Delete an Item
@view_function
def delete(request):
	try:
		item = hmod.Items.objects.get(id=request.urlparams[0])
	except hmod.Items.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')
	
	item.delete()

	return HttpResponseRedirect('/homepage/items/'.format(item.id))









