from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    Products = hmod.Products.objects.filter(isrental=False).filter(isartisan=False)
    RProducts = hmod.Products.objects.filter(isrental=True)

    params['Products'] = Products
    params['RProducts'] = RProducts
    return templater.render_to_response(request, 'productCatalog.html', params)
