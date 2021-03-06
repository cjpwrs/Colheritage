__author__ = 'cjpowers'
from django.conf import settings
from django import forms
from .. import dmp_render, dmp_render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth import authenticate, login
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import random
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType
from django.core.mail import send_mail
import datetime
import random
import requests


@view_function
def process_request(request):
    template_vars = {}
    form = checkoutform()
    if request.method == 'POST':
        form = checkoutform(request.POST)
        API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
        API_KEY = '304b6d2e538424bbc85f749f6be72432'
        # do form.cleaned data, instead of hard coding it in
        r = requests.post(API_URL, data={
            'apiKey': API_KEY,
            'currency': 'usd',
            'amount': '5.99',
            'type': 'Visa',
            'number': '4732817300654',
            'exp_month': '10',
            'exp_year': '15',
            'cvc': '411',
            'name': 'Cosmo Limesandal',
            'description': 'Charge for cosmo@is411.byu.edu'
        })
        print(r.text)

        resp = r.json()
        if 'error' in resp:
            print("ERROR: ", resp['error'])
        else:
            print(resp.keys())
            print(resp['ID'])

        return dmp_render_to_response(request, 'receipt.html', template_vars)

    template_vars['form'] = form
    return dmp_render_to_response(request, 'checkout.html', template_vars)


class checkoutform(forms.Form):
    username = forms.CharField()
    #currency = 'usd'
    amount = '3.99' #get this from session?
    type = forms.CharField(label="Card Type")
    number = forms.CharField(label="Credit Card Number", max_length=16)
    exp_month = forms.CharField(max_length=2)
    exp_year = forms.CharField(max_length=2)
    cvc = forms.CharField(max_length=4)
    #name = 'Cosmo Limesandal'
    #description = 'Charge for cosmo@is411.byu.edu'

    def clean(self):
        username = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data

@view_function
def email(request):
    params = {

    }
    user = hmod.Users.objects.get(id=request.user.id)
    useremail= user.email
    print(1111111111111)



        #email_body = dmp_render(request, 'You have an overdue item that you rented from the Colonial Heritage Foundation. It was due on', params)
    send_mail('Overdue Rental from CHF', 'You have an overdue item that you rented from CHF. It was due on:  and is now  days overdue', 'cjpwrs@gmail.com',
        [useremail], fail_silently=False)
    print(111111111111)
    return dmp_render_to_response(request, 'receipt.html', params)