# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428206939.167545
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/rentals.html'
_template_uri = 'rentals.html'
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
        rental = context.get('rental', UNDEFINED)
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
        rental = context.get('rental', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<div class="clearfix"></div>\n\t<div class="text-right">\n\t\t<a href="/homepage/rentals.create/" class="btn btn-primary">Create New Event </a>\n\t</div>\n\n\t<table class="table table-striped table-bordered">\n\t\t\t<tr>\n\t\t\t\t<th>ID</th>\n\t\t\t\t<th>Date Out</th>\n\t\t\t\t<th>Date Due</th>\n\t\t\t\t<th>Date In</th>\n\t\t\t\t<th>Discount Percent</th>\n\t\t\t\t<th>Rental Product</th>\n                <th>Renter</th>\n                <th>Actions</th>\n\t\t\t</tr>\n')
        for Rented_Item in rental:
            __M_writer('\t\t\t<tr>\n\t\t\t\t<td>')
            __M_writer(str( Rented_Item.id ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( Rented_Item.date_in ))
            __M_writer('</td>\n\t\t\t\t<td>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</td>\n                <td>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</td>\n                <td>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</td>\n\t\t\t\t<td><a href="/homepage/rentals.rentalreturn/')
            __M_writer(str( Rented_Item.id ))
            __M_writer('/" class="btn btn-xs btn-default">Return </a>\n                    <a href="/homepage/rentals.damagefee/" class="btn btn-xs btn-default">Damage Fee </a>\n                </td>\n\n\t\t\t</tr>\n')
        __M_writer('\t</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "rentals.html", "line_map": {"64": 27, "65": 28, "66": 28, "67": 29, "68": 29, "69": 30, "70": 30, "71": 36, "77": 71, "27": 0, "35": 1, "45": 3, "52": 3, "53": 21, "54": 22, "55": 23, "56": 23, "57": 24, "58": 24, "59": 25, "60": 25, "61": 26, "62": 26, "63": 27}, "filename": "/Users/cjpowers/colheritage/homepage/templates/rentals.html"}
__M_END_METADATA
"""
