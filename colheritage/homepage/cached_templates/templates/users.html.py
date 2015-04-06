# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425676105.067232
_enable_loop = True
_template_filename = '/Users/jeffreymccraney/test_dmp/homepage/templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<div class="clearfix"></div>\n\t<div class="text-right">\n\t\t<a href="/homepage/users.create/" class="btn btn-primary">Create New User </a>\n\t</div>\n\n\t<table class="table table-striped table-bordered">\n\t\t\t<tr>\n\t\t\t\t<th>ID</th>\n\t\t\t\t<th>First Name</th>\n\t\t\t\t<th>Last Name</th>\n\t\t\t\t<th>Username</th>\n\t\t\t\t<th>Address</th>\n\t\t\t\t<th>City</th>\n\t\t\t\t<th>State</th>\n\t\t\t\t<th>ZIP</th>\n\t\t\t\t<th>Email</th>\n\t\t\t\t<th>Actions</th>\n\t\t\t</tr>\n')
        for user in users:
            __M_writer('\t\t\t<tr>\n\t\t\t\t<td>')
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
            __M_writer('</td>\n\t\t\t\t<td><a href="/homepage/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/" class="btn btn-xs btn-default">Edit </a></td>\n\t\t\t</tr>\n')
        __M_writer('\t</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 29, "65": 30, "66": 30, "67": 31, "68": 31, "69": 32, "70": 32, "71": 33, "72": 33, "73": 34, "74": 34, "75": 37, "81": 75, "27": 0, "35": 1, "45": 3, "52": 3, "53": 23, "54": 24, "55": 25, "56": 25, "57": 26, "58": 26, "59": 27, "60": 27, "61": 28, "62": 28, "63": 29}, "filename": "/Users/jeffreymccraney/test_dmp/homepage/templates/users.html", "uri": "users.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
