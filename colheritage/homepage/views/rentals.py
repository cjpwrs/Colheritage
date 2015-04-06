__author__ = 'cjpowers'
from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime
import requests
from django.core.mail import send_mail
from .. import dmp_render, dmp_render_to_response

templater = get_renderer('homepage')


####################################################
###### Shows the list of Events

@view_function
def process_request(request):
    params = {}

    rental = hmod.Rented_Item.objects.all()
    params['rental'] = rental


    return templater.render_to_response(request, 'rentals.html', params)

######################################################
###### Edit an Event

@view_function
def edit(request):
    params = {}

    try:
        rental = hmod.Rented_Item.objects.get(id=request.urlparams[0])
    except hmod.Rented_Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    form = RentalEditForm(initial={
        'date_out': rental.date_out,
        'date_due': rental.date_due,
        'discount_percent': rental.discount_percent,
        'rental_product': rental.rental_product,
        'renter' : rental.renter
    })
    if request.method == 'POST':
        form = RentalEditForm(request.POST)
        form.rentalid = rental.id
        if form.is_valid():
            rental.date_out = form.cleaned_data['date_out']
            rental.date_due = form.cleaned_data['date_due']
            rental.discount_percent = form.cleaned_data['discount_percent']
            rental.rental_product = form.cleaned_data['rental_product']
            rental.renter = form.cleaned_data['renter']
            rental.save()
            return HttpResponseRedirect('/homepage/rentals/')




    params['form'] = form
    params['rentals'] = rental
    return templater.render_to_response(request, 'rentals.edit.html', params)

allUsers = hmod.Users.objects.all()
allProducts = hmod.Products.objects.filter(isrental=True)
class RentalEditForm(forms.Form):
    date_out = forms.DateField(label='Date Out (MM/DD/YY)')
    date_due = forms.DateField(label='Date Due (MM/DD/YY)')
    discount_percent = forms.CharField(required = True, max_length = 30)
    rental_product = forms.ModelMultipleChoiceField(queryset=allProducts)
    renter = forms.ModelMultipleChoiceField(queryset=allUsers)



#####################################################
########  Create an Event
@view_function
def create(request):
    rental = hmod.Rented_Item()

    rental.discount_percent = '0.00'
    rental.rental_product = None
    rental.renter = None
    rental.save()

    return HttpResponseRedirect('/homepage/rentals.edit/{}'.format(rental.id))

###################################################
########  Delete a User
@view_function
def delete(request):
    try:
        rental = hmod.Rented_Item.objects.get(id=request.urlparams[0])
    except hmod.Rented_Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    rental.delete()

    return HttpResponseRedirect('/homepage/rentals/'.format(rental.id))


@view_function
def rentalreturn(request):
    params = {}

    try:
        rental = hmod.Rented_Item.objects.get(id=request.urlparams[0])
    except hmod.Rented_Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    form = ReturnForm(initial={
        'date_in': rental.date_in,
    })
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        form.rentalid = rental.id
        if form.is_valid():
            rental.date_in = form.cleaned_data['date_in']
            rental.save()
            return HttpResponseRedirect('/homepage/rentals/')
    params['form'] = form
    params['rentals'] = rental
    return templater.render_to_response(request, 'rentals.rentalreturn.html', params)

class ReturnForm(forms.Form):
    date_in = forms.DateField(label='Date In (MM/DD/YY)')
    damagefee = forms.CharField(max_length = 30)


@view_function
def damagefee(request):
    template_vars = {}

    form = checkoutform()
    if request.method == 'POST':
        form = checkoutform(request.POST)
        if form.is_valid():
            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '304b6d2e538424bbc85f749f6be72432'
            user = hmod.Users.objects.get(username=form.cleaned_data['username'])


            # do form.cleaned data, instead of hard coding it in
            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': form.cleaned_data['amount'],
                'type': form.cleaned_data['type'],
                'number': form.cleaned_data['number'],
                'exp_month': form.cleaned_data['exp_month'],
                'exp_year': form.cleaned_data['exp_year'],
                'cvc': form.cleaned_data['cvc'],
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

            body = dmp_render(request, 'receipt.html', template_vars)

            send_mail('CHF Receipt', body, 'cjpwrs@gmail.com',
            [user.email], fail_silently=False, html_message=body)

            #If it is a rental then make the due date todays date




            return dmp_render_to_response(request, 'receipt.html', template_vars)

    template_vars['form'] = form
    return dmp_render_to_response(request, 'rentals.damagefee.html', template_vars)


class checkoutform(forms.Form):
    username = forms.CharField()
    #currency = 'usd'
    amount = forms.CharField() #get this from session?
    type = forms.CharField(label="Card Type")
    number = forms.CharField(label="Credit Card Number", max_length=16, min_length=10)
    exp_month = forms.CharField(max_length=2, min_length=2)
    exp_year = forms.CharField(max_length=2, min_length=2)
    cvc = forms.CharField(max_length=4, label="CVC", min_length=3)
    #name = 'Cosmo Limesandal'
    #description = 'Charge for cosmo@is411.byu.edu'








