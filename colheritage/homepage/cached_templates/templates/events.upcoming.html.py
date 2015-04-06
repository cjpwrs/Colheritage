# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428164512.381894
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/events.upcoming.html'
_template_uri = 'events.upcoming.html'
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
        Events = context.get('Events', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        Events = context.get('Events', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<div class="clearfix"></div>\n\n\n<title>Upcoming Events</title>\n<h1>Upcoming Events</h1>\n\n')
        for event in Events:
            __M_writer('\t    <div class="eventblock">\n\n\t\t\t\t<h1>')
            __M_writer(str( event.name ))
            __M_writer('</h1>\n                <img src="/static/homepage/media/events/boston.jpg" class="eventimage" alt="Boston"\n\t\t\t\t<div class = "eventbody">\n                    <br><strong>Description:</strong>')
            __M_writer(str( event.description ))
            __M_writer('\n\t\t\t\t    <br><strong>When: </strong>')
            __M_writer(str( event.startDate ))
            __M_writer('\n                    <br><strong>Where: </strong><a href="')
            __M_writer(str( event.mapURL ))
            __M_writer('" class="btn btn-primary">Map </a>\n                    <br><a href="/homepage/areas/" class="btn btn-primary">Click here to explore the areas at this event </a>\n                    <br><a href="/homepage/artisanCatalog/" class="btn btn-primary">Click here to see artisan products that will be at the event </a>\n                </div>\n        </div>\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 11, "54": 12, "55": 14, "56": 14, "57": 17, "58": 17, "59": 18, "60": 18, "61": 19, "62": 19, "63": 25}, "source_encoding": "ascii", "filename": "/Users/cjpowers/colheritage/homepage/templates/events.upcoming.html", "uri": "events.upcoming.html"}
__M_END_METADATA
"""
