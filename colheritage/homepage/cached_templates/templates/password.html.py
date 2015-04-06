# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425679209.26958
_enable_loop = True
_template_filename = '/Users/jeffreymccraney/test_dmp/homepage/templates/password.html'
_template_uri = 'password.html'
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<table class="table table-striped table-bordered">\n\t\t\t<tr>\n\t\t\t\t<th>ID</th>\n\t\t\t\t<th>First Name</th>\n\t\t\t\t<th>Last Name</th>\n\t\t\t\t<th>Username</th>\n\t\t\t\t<th>Address</th>\n\t\t\t\t<th>City</th>\n\t\t\t\t<th>State</th>\n\t\t\t\t<th>ZIP</th>\n\t\t\t\t<th>Email</th>\n\t\t\t\t<th>Actions</th>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>')
        __M_writer(str( user.id ))
        __M_writer('</td>\n\t\t\t\t<td>')
        __M_writer(str( user.first_name ))
        __M_writer('</td>\n\t\t\t\t<td>')
        __M_writer(str( user.last_name ))
        __M_writer('</td>\n\t\t\t\t<td>')
        __M_writer(str( user.username ))
        __M_writer('</td>\n\t\t\t\t<td>')
        __M_writer(str( user.address1 ))
        __M_writer('</td>\n\t\t\t\t<td>')
        __M_writer(str( user.city ))
        __M_writer('</td>\n\t\t\t\t<td>')
        __M_writer(str( user.state ))
        __M_writer('</td>\n\t\t\t\t<td>')
        __M_writer(str( user.zip ))
        __M_writer('</td>\n\t\t\t\t<td>')
        __M_writer(str( user.email ))
        __M_writer('</td>\n\t\t\t\t<td><a href="/homepage/password.edit/')
        __M_writer(str( user.id ))
        __M_writer('/" class="btn btn-xs btn-default">Edit </a></td>\n\t\t\t</tr>\n\t</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jeffreymccraney/test_dmp/homepage/templates/password.html", "source_encoding": "ascii", "uri": "password.html", "line_map": {"64": 24, "65": 25, "66": 25, "67": 26, "68": 26, "69": 27, "70": 27, "71": 28, "72": 28, "78": 72, "27": 0, "35": 1, "45": 3, "52": 3, "53": 19, "54": 19, "55": 20, "56": 20, "57": 21, "58": 21, "59": 22, "60": 22, "61": 23, "62": 23, "63": 24}}
__M_END_METADATA
"""
