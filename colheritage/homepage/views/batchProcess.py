from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import random
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
import datetime
from django.core.mail import send_mail
from time import time


@view_function
def process_request(request):
    template_vars = {}

    items = hmod.Rented_Item.objects.all()
    print(items)
    overdueitems = hmod.Rented_Item.objects.exclude(date_in__isnull=False)
    print(111111111111111)
    print(overdueitems)
    print(22222222222222)
    template_vars['sixty'] = []
    template_vars['thirty'] = []
    template_vars['zero'] = []

    for Rented_Item in overdueitems:
        ds = datetime.date.today() - Rented_Item.date_due
        dt = abs(ds.days)
        print(ds)
        print(dt)
        if dt >= 60:
            sixty = Rented_Item
            print(sixty)
            template_vars['sixty'].append(Rented_Item)
            print(Rented_Item.renter)

        elif dt < 60 & dt >= 30:
            thirty = Rented_Item
            print(thirty)
            template_vars['thirty'].append(Rented_Item)


        else:
            zero = Rented_Item
            print(zero)
            template_vars['zero'].append(Rented_Item)



    template_vars['overdueitems'] = overdueitems
    return dmp_render_to_response(request, 'batchProcess.html', template_vars)


@view_function
def email(request):
    params = {

    }
    overdueitems = hmod.Rented_Item.objects.exclude(date_in__isnull=False)
    print(1111111111111)
    for Rented_Item in overdueitems:
        ds = datetime.date.today() - Rented_Item.date_due
        dt = abs(ds.days)
        print(111111111111)

        #email_body = dmp_render(request, 'You have an overdue item that you rented from the Colonial Heritage Foundation. It was due on', params)
        send_mail('Overdue Rental from CHF', 'You have an overdue item that you rented from CHF. It was due on: %s and is now %s days overdue' % (Rented_Item.date_due, dt), 'spencerw.smith.byu@gmail.com',
            [Rented_Item.renter.email], fail_silently=False)

    return dmp_render_to_response(request, 'batchprocessemail.html', params)
