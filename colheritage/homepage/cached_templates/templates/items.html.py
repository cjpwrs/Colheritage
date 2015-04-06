# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423333222.228997
_enable_loop = True
_template_filename = '/Users/jeffreymccraney/test_dmp/homepage/templates/items.html'
_template_uri = 'items.html'
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
        Items = context.get('Items', UNDEFINED)
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
        Items = context.get('Items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<div class="clearfix"></div>\n\t<div class="text-right">\n\t\t<a href="/homepage/items.create/" class="btn btn-primary">Create a New Item </a>\n\t</div>\n\n\t<table class="table table-striped table-bordered">\n\t\t\t<tr>\n\t\t\t\t<th>ID</th>\n\t\t\t\t<th>Item Name</th>\n\t\t\t\t<th>Description</th>\n\t\t\t\t<th>Value</th>\n\t\t\t\t<th>Standard Rental Price</th>\n\t\t\t\t<th>Actions</th>\n\t\t\t</tr>\n')
        for item in Items:
            __M_writer('\t\t\t<tr>\n\t\t\t\t<td>')
            __M_writer(str( item.id ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( item.name ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( item.description ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( item.value ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( item.standardRentalPrice ))
            __M_writer('</td>\n\t\t\t\t<td><a href="/homepage/items.edit/')
            __M_writer(str( item.id ))
            __M_writer('/" class="btn btn-xs btn-default">Edit </a></td>\n\t\t\t</tr>\n')
        __M_writer('\t</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 25, "65": 26, "66": 26, "35": 1, "73": 67, "45": 3, "27": 0, "67": 29, "52": 3, "53": 19, "54": 20, "55": 21, "56": 21, "57": 22, "58": 22, "59": 23, "60": 23, "61": 24, "62": 24, "63": 25}, "uri": "items.html", "source_encoding": "ascii", "filename": "/Users/jeffreymccraney/test_dmp/homepage/templates/items.html"}
__M_END_METADATA
"""
