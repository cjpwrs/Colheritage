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

	try:
		product = hmod.Products.objects.get(id=request.urlparams[0])
	except hmod.Products.DoesNotExist:
		return HttpResponseRedirect('/homepage/productCatalog/')

	params['product'] = product
	return templater.render_to_response(request, 'details.html', params)











