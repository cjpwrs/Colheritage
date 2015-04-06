# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423336783.454969
_enable_loop = True
_template_filename = '/Users/jeffreymccraney/test_dmp/homepage/templates/historical.html'
_template_uri = 'historical.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        HistoricalFigures = context.get('HistoricalFigures', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        HistoricalFigures = context.get('HistoricalFigures', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t<p>The Following is a list of Historical Figures represented in the Festival</p>\n\t<div class="clearfix"></div>\n\t<div class="text-right">\n\t\t<a href="/homepage/historical.create/" class="btn btn-primary">Create a New Historical Figure </a>\n\t</div>\n\n\t<table class="table table-striped table-bordered">\n\t\t\t<tr>\n\t\t\t\t<th>ID</th>\n\t\t\t\t<th>Name</th>\n\t\t\t\t<th>Birth Date</th>\n\t\t\t\t<th>Birth Place</th>\n\t\t\t\t<th>Death Date</th>\n\t\t\t\t<th>Death Place</th>\n\t\t\t\t<th>Biographical Note</th>\n\t\t\t\t<th>Fictional?</th>\n\t\t\t\t<th>Actions</th>\n\t\t\t</tr>\n')
        for historicalFigure in HistoricalFigures:
            __M_writer('\t\t\t<tr>\n\t\t\t\t<td>')
            __M_writer(str( historicalFigure.id ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( historicalFigure.name ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( historicalFigure.birthDate ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( historicalFigure.birthPlace ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( historicalFigure.deathDate ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( historicalFigure.deathPlace ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( historicalFigure.biographicalNote ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( historicalFigure.isFictional ))
            __M_writer('</td>\n\t\t\t\t<td><a href="/homepage/historical.edit/')
            __M_writer(str( historicalFigure.id ))
            __M_writer('/" class="btn btn-xs btn-default">Edit </a></td>\n\t\t\t</tr>\n')
        __M_writer('\t</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/jeffreymccraney/test_dmp/homepage/templates/historical.html", "line_map": {"64": 28, "65": 29, "66": 29, "67": 30, "68": 30, "69": 31, "70": 31, "71": 32, "72": 32, "73": 35, "79": 73, "27": 0, "35": 1, "45": 3, "52": 3, "53": 22, "54": 23, "55": 24, "56": 24, "57": 25, "58": 25, "59": 26, "60": 26, "61": 27, "62": 27, "63": 28}, "uri": "historical.html"}
__M_END_METADATA
"""
