from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


######################################################
###### Shows the list of Historical Figures

@view_function
def process_request(request):
	params = {}

	HistoricalFigures = hmod.HistoricalFigures.objects.all().order_by('name')
	params['HistoricalFigures'] = HistoricalFigures


	return templater.render_to_response(request, 'historical.html', params)

######################################################
###### Edit a Historical Figure
@view_function
def edit(request):
	params = {}

	try:
		historicalFigure = hmod.HistoricalFigures.objects.get(id=request.urlparams[0])
	except hmod.HistoricalFigures.DoesNotExist:
		return HttpResponseRedirect('/homepage/events/')

	form = HistoricalFigureEditForm(initial={
		'name': historicalFigure.name,
		'birthDate': historicalFigure.birthDate,
		'birthPlace': historicalFigure.birthPlace,
		'deathDate': historicalFigure.deathDate,
		'deathPlace': historicalFigure.deathPlace,
		'biographicalNote': historicalFigure.biographicalNote,
		'isFictional': historicalFigure.isFictional,
	})
	if request.method == 'POST':
		form = HistoricalFigureEditForm(request.POST)
		form.historicalFigureid = historicalFigure.id
		if form.is_valid():
			historicalFigure.name = form.cleaned_data['name']
			historicalFigure.birthDate = form.cleaned_data['birthDate']
			historicalFigure.birthPlace = form.cleaned_data['birthPlace']
			historicalFigure.deathDate = form.cleaned_data['deathDate']
			historicalFigure.deathPlace = form.cleaned_data['deathPlace']
			historicalFigure.biographicalNote = form.cleaned_data['biographicalNote']
			historicalFigure.isFictional = form.cleaned_data['isFictional']
			historicalFigure.save()
			return HttpResponseRedirect('/homepage/historical/')  		




	params['form'] = form
	params['historicalFigure'] = historicalFigure
	return templater.render_to_response(request, 'historical.edit.html', params)

class HistoricalFigureEditForm(forms.Form):
	name = forms.CharField(required = True, max_length = 100)
	birthDate = forms.CharField(required = True, max_length = 30)
	birthPlace = forms.CharField(required = True, max_length = 100)
	deathDate = forms.CharField(required = True, max_length = 30)
	deathPlace = forms.CharField(required = True, max_length = 100)
	biographicalNote = forms.CharField(required = True, max_length = 300)
	isFictional = forms.CharField(required = True, max_length = 10)


#####################################################
########  Create a Historical Figure
@view_function
def create(request):
	historicalFigure = hmod.HistoricalFigures()
	historicalFigure.name = ''
	historicalFigure.birthDate = ''
	historicalFigure.birthPlace = ''
	historicalFigure.deathDate = ''
	historicalFigure.deathPlace = ''
	historicalFigure.biographicalNote = ''
	historicalFigure.isFictional = ''
	historicalFigure.save()

	return HttpResponseRedirect('/homepage/historical.edit/{}'.format(historicalFigure.id))

#####################################################
########  Delete a Historical Figure
@view_function
def delete(request):
	try:
		historicalFigure = hmod.HistoricalFigures.objects.get(id=request.urlparams[0])
	except hmod.HistoricalFigures.DoesNotExist:
		return HttpResponseRedirect('/homepage/historical/')
	
	historicalFigure.delete()

	return HttpResponseRedirect('/homepage/historical/'.format(historicalFigure.id))









