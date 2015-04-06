from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime

templater = get_renderer('homepage')


######################################################
###### Shows the list of Events

@view_function
def process_request(request):
	params = {}

	Events = hmod.Events.objects.all().order_by('name')
	params['Events'] = Events


	return templater.render_to_response(request, 'events.html', params)

######################################################
###### Edit an Event

@view_function
def edit(request):
	params = {}

	try:
		event = hmod.Events.objects.get(id=request.urlparams[0])
	except hmod.Events.DoesNotExist:
		return HttpResponseRedirect('/homepage/events/')

	form = EventEditForm(initial={
		'name': event.name,
		'description': event.description,
		'start_Date': event.startDate,
		'end_Date': event.endDate,
		'map_Location': event.mapFileName,
	})
	if request.method == 'POST':
		form = EventEditForm(request.POST)
		form.eventid = event.id
		if form.is_valid():
			event.name = form.cleaned_data['name']
			event.description = form.cleaned_data['description']
			event.startDate = form.cleaned_data['start_Date']
			event.endDate = form.cleaned_data['end_Date']
			event.mapFileName = form.cleaned_data['map_Location']
			event.save()
			return HttpResponseRedirect('/homepage/events/')  		




	params['form'] = form
	params['event'] = event
	return templater.render_to_response(request, 'events.edit.html', params)

class EventEditForm(forms.Form):
	name = forms.CharField(required = True, max_length = 100)
	description = forms.CharField(required = True, max_length = 300)
	start_Date = forms.CharField(required = True, max_length = 30)
	end_Date = forms.CharField(required = True, max_length = 30)
	map_Location = forms.CharField(max_length=100)

#####################################################
########  Create an Event
@view_function
def create(request):
	event = hmod.Events()
	event.name = ''
	event.description = ''
	event.startDate = ''
	event.endDate = ''
	event.mapFileName = ''
	event.save()

	return HttpResponseRedirect('/homepage/events.edit/{}'.format(event.id))

#####################################################
########  Delete a User
@view_function
def delete(request):
	try:
		event = hmod.Events.objects.get(id=request.urlparams[0])
	except hmod.Events.DoesNotExist:
		return HttpResponseRedirect('/homepage/events/')
	
	event.delete()

	return HttpResponseRedirect('/homepage/events/'.format(event.id))


#################################################################################3
### UPCOMING EVENTS

@view_function
def upcoming(request):
	params = {}

	Events = hmod.Events.objects.filter(startDate__gt=datetime.date.today())
	params['Events'] = Events


	return templater.render_to_response(request, 'events.upcoming.html', params)









