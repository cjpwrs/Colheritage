# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427990885.903788
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/password_reset_form.html'
_template_uri = 'password_reset_form.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('{% extends "base.htm" %}\n{% load i18n %}\n\n{% block breadcrumbs %}\n<div class="breadcrumbs">\n<a href="{% url \'admin:index\' %}">{% trans \'Home\' %}</a>\n&rsaquo; {% trans \'Password reset\' %}\n</div>\n{% endblock %}\n\n{% block title %}{{ title }}{% endblock %}\n{% block content_title %}<h1>{{ title }}</h1>{% endblock %}\n{% block content %}\n\n<p>{% trans "Forgotten your password? Enter your email address below, and we\'ll email instructions for setting a new one." %}</p>\n\n<form action="" method="post">{% csrf_token %}\n{{ form.email.errors }}\n<p><label for="id_email">{% trans \'Email address:\' %}</label> {{ form.email }} <input type="submit" value="{% trans \'Reset my password\' %}" /></p>\n</form>\n\n{% endblock %}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "27": 21, "21": 1}, "filename": "/Users/cjpowers/colheritage/homepage/templates/password_reset_form.html", "uri": "password_reset_form.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
