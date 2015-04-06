from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
import homepage.models as hmod

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    return templater.render_to_response(request, 'index.html', params)


#@view_function
#def loginform(request):
#    params = {}

#    form = LoginForm()
#    if request.method == 'POST':
#       form = LoginForm(request.POST)
#       if form.is_valid():
#        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#        login(request, user)

#   params['form'] = form
#   return templater.render_to_response(request, 'index2.loginform.html', params)



#############################
## Login

@view_function
def loginform(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
       #user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
       #login(request, user)

        username=form.cleaned_data['username']
        password=form.cleaned_data['password']

        s = Server('colheritagefoundation.info', port = 8484, get_info = GET_ALL_INFO)
        print(1111111111111111111111111111111111)
        c = Connection(s, auto_bind = True, client_strategy = STRATEGY_SYNC,

        user='TA@colheritagefoundation.local',password ='mordor', authentication = AUTH_SIMPLE)

        print('***************************************1')
        print(c)
        print('***************************************2')
        print(c.user)
        print('***************************************3')
       #if c != None:

        #user = hmod.Users.objects.create_user(
        #username=form.cleaned_data['username']
        #)
        #user.set_password(form.cleaned_data['password'])
        #user.save()
       #user = authenticate(form.cleanded_data['username'], password=form.cleaned_data['password'])
       #login(request, user)


       #else:
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)


        return HttpResponse('''
          <script>
            window.location.href = '/homepage/index/   ';
          </script>
        ''')
       #return HttpResponseRedirect('/homepage/account/')

    params['form'] = form
    return templater.render_to_response(request, 'index.loginform.html', params)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(label = "Password", widget=forms.PasswordInput )

 #def clean(self):
 #   user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
 #   if user == None:
 #       raise forms.ValidationError("Incorrect username or password")
 #   return self.cleaned_data
