# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428170628.784841
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/batchProcess.html'
_template_uri = 'batchProcess.html'
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
        thirty = context.get('thirty', UNDEFINED)
        zero = context.get('zero', UNDEFINED)
        sixty = context.get('sixty', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        thirty = context.get('thirty', UNDEFINED)
        zero = context.get('zero', UNDEFINED)
        sixty = context.get('sixty', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<title>Overdue Rentals</title>\n<h1>Overdue Rentals</h1>\n\n<a href="/homepage/batchProcess.email/" class="btn btn-warning">Send Emails</a>\n  <table>\n   <tr>\n      <th>Renter\'s Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\n      <th>Rental Product</th>\n\n  </tr>\n<h1>Items overdue by 60 days or more</h1>\n')
        for Rented_Item in sixty:
            __M_writer('       <tr>\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\n            <p></p>\n       </tr>\n')
        __M_writer("  </table>\n<br>\n<br>\n<br>\n\n <table>\n   <tr>\n      <h1>Items overdue between 30 and 60 days</h1>\n      <th>Renter's Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\n      <th>Rental Product</th>\n\n  </tr>\n\n")
        for Rented_Item in thirty:
            __M_writer('       <tr>\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\n            <p></p>\n       </tr>\n')
        __M_writer("  </table>\n<br>\n<br>\n<br>\n\n <table>\n   <tr>\n      <h1>Items overdue for 30 days or less</h1>\n      <th>Renter's Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Out&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Date Due&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n      <th>Discount Percent&nbsp;&nbsp;&nbsp;</th>\n      <th>Rental Product</th>\n  </tr>\n\n")
        for Rented_Item in zero:
            __M_writer('       <tr>\n\n            <th>')
            __M_writer(str( Rented_Item.renter ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_out ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.date_due ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.discount_percent ))
            __M_writer('</th>\n            <th>')
            __M_writer(str( Rented_Item.rental_product ))
            __M_writer('</th>\n            <p></p>\n       </tr>\n')
        __M_writer('  </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "37": 1, "47": 4, "56": 4, "57": 19, "58": 20, "59": 21, "60": 21, "61": 22, "62": 22, "63": 23, "64": 23, "65": 24, "66": 24, "67": 25, "68": 25, "69": 29, "70": 45, "71": 46, "72": 47, "73": 47, "74": 48, "75": 48, "76": 49, "77": 49, "78": 50, "79": 50, "80": 51, "81": 51, "82": 55, "83": 70, "84": 71, "85": 73, "86": 73, "87": 74, "88": 74, "89": 75, "90": 75, "91": 76, "92": 76, "93": 77, "94": 77, "95": 81, "101": 95}, "uri": "batchProcess.html", "filename": "/Users/cjpowers/colheritage/homepage/templates/batchProcess.html"}
__M_END_METADATA
"""
