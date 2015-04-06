# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427878879.565892
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/rentalCatalog.html'
_template_uri = 'rentalCatalog.html'
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
        Rental_Product = context.get('Rental_Product', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        Rental_Product = context.get('Rental_Product', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('    <br>\n    <div class="text-right">\n        Search Rentals: <input type="search" id="searchRentals">\n    </div>\n    ')


    

        __M_writer('\n\n    \t<div class="rental_container">\n    \t<a href="/homepage/details/')
        __M_writer(str( Rental_Product.id ))
        __M_writer('/">\n    \t<img class="" src="')
        __M_writer(str(STATIC_URL))
        __M_writer(str(Rental_Product.image))
        __M_writer('" />\n    \t<div class="text-muted text-center productName">')
        __M_writer(str( Rental_Product.name ))
        __M_writer('</div>\n    \t<div class="text-muted text-center">')
        __M_writer(str( Rental_Product.currentPrice ))
        __M_writer('</div>\n    \t</a>\n    \t\t<div class="text-right">\n            Qty: <input type="number" class="qty" name="qty" value="1">\n    \t\t  <button data-pid="')
        __M_writer(str( Rental_Product.id ))
        __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button>\n    \t\t</div>\n    \t</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 15, "65": 15, "66": 16, "67": 16, "36": 1, "69": 17, "70": 21, "71": 21, "77": 71, "46": 3, "54": 3, "55": 5, "56": 9, "68": 17, "27": 0, "60": 11, "61": 14, "62": 14, "63": 15}, "uri": "rentalCatalog.html", "filename": "/Users/cjpowers/colheritage/homepage/templates/rentalCatalog.html"}
__M_END_METADATA
"""
