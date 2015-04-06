# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428020137.125198
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/index.loginform.html'
_template_uri = 'index.loginform.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t<div class="content">\n\n\t\t\t<form id="loginform" method="POST" action="/homepage/index.loginform">\n\t\t\t\t<table>\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t\t\t\t</table>\n\t\t\t\t<input type="submit">\n\t\t\t</form>\n\t\t\tNot a User?<a href="/homepage/accounts.create/">Register Here!</a><br>\n            <a href="/password_reset/">Reset Password</a>\n\t\t</div>\n\n\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "53": 4, "54": 9, "55": 9, "40": 19, "27": 0, "61": 55, "46": 4}, "uri": "index.loginform.html", "filename": "/Users/cjpowers/colheritage/homepage/templates/index.loginform.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
