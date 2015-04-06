# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428206823.03359
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/checkout.html'
_template_uri = 'checkout.html'
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
        __M_writer('\n')
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
        __M_writer('\n    <h1>Checkout</h1>\n')
        if user.is_authenticated() :
            __M_writer('    <form method="POST">\n    <table>\n    ')
            __M_writer(str( form ))
            __M_writer('\n    </table>\n    <br>\n    <a href= "/homepage/receipt.email/"><button type="submit" class="btn btn-primary">Purchase</button><a>\n    </form>\n\n')
        else:
            __M_writer('    <div id="login">\n    <strong>You will need to login first in order to checkout, thank you.</strong>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "checkout.html", "line_map": {"66": 60, "59": 13, "36": 1, "54": 2, "55": 4, "56": 5, "57": 7, "58": 7, "27": 0, "60": 14, "46": 2}, "filename": "/Users/cjpowers/colheritage/homepage/templates/checkout.html"}
__M_END_METADATA
"""
