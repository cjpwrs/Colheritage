# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423347125.029723
_enable_loop = True
_template_filename = '/Users/jeffreymccraney/test_dmp/homepage/templates/users.edit.html'
_template_uri = 'users.edit.html'
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
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t<form method="POST">\n\t<h4>Re-Enter User Password</h4>\n\t<table>\t\n\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t</table>\n\t<button type="submit" class="btn btn-primary">Submit</button>\n\t<a href="/homepage/users.delete/')
        __M_writer(str( user.id ))
        __M_writer('/">Delete Account</a>\n\t</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 58, "36": 1, "54": 3, "55": 8, "56": 8, "57": 11, "58": 11, "27": 0, "46": 3}, "filename": "/Users/jeffreymccraney/test_dmp/homepage/templates/users.edit.html", "uri": "users.edit.html"}
__M_END_METADATA
"""
