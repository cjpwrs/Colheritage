from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from .. import dmp_render, dmp_render_to_response
import requests
from django.core.mail import send_mail


templater = get_renderer('homepage')


@view_function
def process_request(request):
    template_vars = {}

    # get the items in the shopping cart in an ajax ($.loadmodal) dialogg

    cart_Products = {}

    cart_Products = request.session['shopping_cart']

    current_cart = {}

    for product, value in cart_Products.items():
        item = hmod.Products.objects.get(id=product)
        product_container = []
        product_container.append(item)
        product_container.append(value)
        current_cart[item.id] = product_container

    template_vars['current_cart'] = current_cart

    return templater.render_to_response(request, 'shoppingCart.html', template_vars)


@view_function
def add(request):
    #when they click the add button

    #ensure that we have a shopping cart in the session
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
        print ('New Shopping Cart Created')
    # add the item to the shopping cart
    pid = request.urlparams[0]
    qty = int(request.urlparams[1])

    if pid in request.session['shopping_cart']:
        request.session['shopping_cart'][pid] += qty
        request.session.modified = True
    else:
        request.session['shopping_cart'][pid] = qty
        request.session.modified = True

    params = {}

    return HttpResponseRedirect('/homepage/shoppingCart/')


@view_function
def delete(request):
    pid = request.urlparams[0]
    del request.session['shopping_cart'][pid]

    request.session.modified = True

    return HttpResponseRedirect('/homepage/shoppingCart')


@view_function
def addform(request):
    template_vars = {}

    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        return HttpResponse('''
             <script>
              window.location.href = '/homepage/shoppingcart';
             </script>
              ''')

    template_vars['form'] = form
    return dmp_render_to_response(request, 'shoppingcart.addform.html', template_vars)


class AddForm(forms.Form):
    QTY = forms.CharField()


@view_function
def checkout(request):
    template_vars = {}

    form = checkoutform()
    if request.method == 'POST':
        form = checkoutform(request.POST)
        if form.is_valid():
            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '304b6d2e538424bbc85f749f6be72432'
            user = hmod.Users.objects.get(username=form.cleaned_data['username'])

            #Get shopping cart info to get total price and send receipt
            cart = request.session["shopping_cart"]
            print(str(cart))

            template_vars['productlist'] = []
            template_vars['pricelist'] = []
            totalprice = 0

            for key, qty in cart.items():
                product = hmod.Products.objects.get(id=key)
                price = product.currentPrice * qty
                totalprice = totalprice + price
                name = product.name
                print(name)
                print(price)
                template_vars['productlist'].append([name, price])
                template_vars['pricelist'].append(price)

            #for loop to take out each product in productlist
            template_vars['tp'] = totalprice

            # do form.cleaned data, instead of hard coding it in
            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': totalprice,
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
    return dmp_render_to_response(request, 'checkout.html', template_vars)


class checkoutform(forms.Form):
    username = forms.CharField()
    #currency = 'usd'
    #amount = forms.CharField() #get this from session?
    type = forms.CharField(label="Card Type")
    number = forms.CharField(label="Credit Card Number", max_length=16, min_length=10)
    exp_month = forms.CharField(max_length=2, min_length=2)
    exp_year = forms.CharField(max_length=2, min_length=2)
    cvc = forms.CharField(max_length=4, label="CVC", min_length=3)
    #name = 'Cosmo Limesandal'
    #description = 'Charge for cosmo@is411.byu.edu'

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'))

        return self.cleaned_data





