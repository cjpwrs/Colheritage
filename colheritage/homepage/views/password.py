from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


templater = get_renderer('homepage')


######################################################
###### Shows the list of Users

@view_function
def process_request(request):
	params = {}

	users = hmod.Users.objects.all().order_by('last_name','first_name')
	params['users'] = users


	return templater.render_to_response(request, 'password.html', params)


######################################################
###### Edit a User

@view_function
def edit(request):
	params = {}

	try:
		user = hmod.Users.objects.get(id=request.urlparams[0])
	except hmod.Users.DoesNotExist:
		return HttpResponseRedirect('/homepage/index/')

	form = PasswordEditForm(initial={
		'username': user.username,
		'password': user.password,
	})
	if request.method == 'POST':
		form = PasswordEditForm(request.POST)
		form.userid = user.id
		if form.is_valid():
			user.username  = form.cleaned_data['username']
			user.set_password(form.cleaned_data['password'])
			user.save()
			return HttpResponseRedirect('/homepage/index/')  		




	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'password.edit.html', params)

class PasswordEditForm(forms.Form):
	username = forms.CharField(required = True, max_length=100)
	password = forms.CharField(required =True, max_length=100, widget=forms.PasswordInput)

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
	)

	return HttpResponseRedirect('/homepage/password.edit/{}'.format(user.id))

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


