from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, logout
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('homepage')


########## Login ####################

@view_function
def process_request(request):
    params = {}
    logout(request)
    return HttpResponseRedirect('/homepage/index/')

