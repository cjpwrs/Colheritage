from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE, GET_ALL_INFO

templater = get_renderer('homepage')


########## Login ####################

@view_function
def process_request(request):
    params = {}



    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/homepage/users/')         


    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label="Password", required = True, widget=forms.PasswordInput)


    def clean(self):
        username = self.cleaned_data['username']
        password=self.cleaned_data['password']
        #check the employee against Active Directory
        # define the server and the connection
        s = Server('128.187.61.49', port = 389, get_info = GET_ALL_INFO)
        c = Connection(s, auto_bind = True, client_strategy = STRATEGY_SYNC, user=username, password=password, authentication=AUTH_SIMPLE)
        print(s.info) # display info from the DSE. OID are decoded when recognized by the library

        user = authenticate(username=username, password=password)
        if user == None:
            raise forms.ValidationError('Username and Password do not match')
        return self.cleaned_data
