from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType


templater = get_renderer('homepage')


######################################################
###### Shows the list of Users

@view_function
def process_request(request):
	params = {}

	users = hmod.Users.objects.all().order_by('last_name','first_name')
	params['users'] = users


	return templater.render_to_response(request, 'accounts.html', params)


######################################################
###### Edit a User

@view_function
def edit(request):
	params = {}

	try:
		user = hmod.Users.objects.get(id=request.urlparams[0])
	except hmod.Users.DoesNotExist:
		return HttpResponseRedirect('/homepage/index/')

	form = UserEditForm(initial={
		'first_name': user.first_name,
		'last_name': user.last_name,
		'username': user.username,
		'password': user.password,
		'address': user.address1,
		'city': user.city,
		'state': user.state,
		'zip': user.zip,
		'email': user.email,
	})
	if request.method == 'POST':
		form = UserEditForm(request.POST)
		form.userid = user.id
		if form.is_valid():
			user.first_name  = form.cleaned_data['first_name']
			user.last_name  = form.cleaned_data['last_name']
			user.username  = form.cleaned_data['username']
			user.set_password(form.cleaned_data['password'])
			user.address1  = form.cleaned_data['address']
			user.city  = form.cleaned_data['city']
			user.state  = form.cleaned_data['state']
			user.zip  = form.cleaned_data['zip']
			user.email  = form.cleaned_data['email']
			user.save()
			return HttpResponseRedirect('/homepage/index/')  		




	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'accounts.edit.html', params)

class UserEditForm(forms.Form):
	first_name = forms.CharField(required = True, max_length = 100)
	last_name = forms.CharField(required = True, max_length=100)
	username = forms.CharField(required = True, max_length=100)
	password = forms.CharField(required =True, max_length=100, widget=forms.PasswordInput)
	address = forms.CharField(required = True, max_length=100)
	city = forms.CharField(required = True, max_length=100)
	state = forms.CharField(required = True, max_length=2)
	zip = forms.CharField(required = True, max_length=5)
	email = forms.EmailField(required = True, max_length=100)

	def clean_username(self):
		user = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid)
		if len(user) >= 1:
			raise forms.ValidationError("This Username is already taken. Please enter another!")

		return self.cleaned_data['username']
#####################################################
########  Create a User
@view_function
#@permission_required('homepage.add_users')
def create(request):
	user = hmod.Users.objects.create_user(
		username = 'Enter Username',
		password = '',
		first_name = '',
		last_name = '',
		address1 = '',
		city = '',
		state = '',
		zip = '',
		email = '',
	)

	return HttpResponseRedirect('/homepage/accounts.edit/{}'.format(user.id))

#####################################################
########  Delete a User
@view_function
def delete(request):
	try:
		user = hmod.Users.objects.get(id=request.urlparams[0])
	except hmod.Users.DoesNotExist:
		return HttpResponseRedirect('/homepage/index/')
	
	user.delete()

	return HttpResponseRedirect('/homepage/index/'.format(user.id))







