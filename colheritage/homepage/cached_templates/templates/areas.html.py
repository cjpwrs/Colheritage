# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428072408.520993
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/areas.html'
_template_uri = 'areas.html'
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
        Areas = context.get('Areas', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        Areas = context.get('Areas', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('    <br>\n    <div class="text-right">\n\n    </div>\n    ')


    

        __M_writer('\n')
        for Area in Areas:
            __M_writer('    \t<div class="area_container">\n    \t    <img class="" src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str(Area.image))
            __M_writer('" />\n    \t    <div class="text-muted text-center areaName"><strong>')
            __M_writer(str( Area.name ))
            __M_writer('</strong></div>\n    \t    <div class="text-muted text-center">')
            __M_writer(str( Area.description ))
            __M_writer('</div>\n\n\n    \t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/cjpowers/colheritage/homepage/templates/areas.html", "uri": "areas.html", "source_encoding": "ascii", "line_map": {"64": 14, "65": 14, "66": 15, "67": 15, "36": 1, "69": 16, "75": 69, "46": 3, "54": 3, "55": 5, "56": 9, "68": 16, "27": 0, "60": 11, "61": 12, "62": 13, "63": 14}}
__M_END_METADATA
"""
