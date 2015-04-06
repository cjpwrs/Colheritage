# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428165022.728549
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/productCatalog.html'
_template_uri = 'productCatalog.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        Products = context.get('Products', UNDEFINED)
        RProducts = context.get('RProducts', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        Products = context.get('Products', UNDEFINED)
        RProducts = context.get('RProducts', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('    <br>\n    <div class="text-right">\n        Search Products: <input type="search" id="searchProducts">\n    </div>\n    ')


    

        __M_writer('\n    <h1>Products for Purchase</h1>\n')
        for Product in Products:
            __M_writer('    \t<div class="item_container">\n    \t<a href="/homepage/details/')
            __M_writer(str( Product.id ))
            __M_writer('/">\n    \t<img class="" src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str(Product.image))
            __M_writer('" />\n    \t<div class="text-muted text-center productName">')
            __M_writer(str( Product.name ))
            __M_writer('</div>\n    \t<div class="text-muted text-center">')
            __M_writer(str( Product.currentPrice ))
            __M_writer('</div>\n    \t</a>\n    \t\t<div class="text-right">\n            Qty: <input type="number" class="qty" name="qty" value="1">\n    \t\t  <button data-pid="')
            __M_writer(str( Product.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button>\n    \t\t</div>\n    \t</div>\n')
        __M_writer('\n    <h1>Products for Rental</h1>\n')
        for Product in RProducts:
            __M_writer('            <div class="item_container">\n            <a href="/homepage/details/')
            __M_writer(str( Product.id ))
            __M_writer('/">\n            <img class="" src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str(Product.image))
            __M_writer('" />\n            <div class="text-muted text-center productName">')
            __M_writer(str( Product.name ))
            __M_writer('</div>\n            <div class="text-muted text-center">')
            __M_writer(str( Product.currentPrice ))
            __M_writer('</div>\n            </a>\n                <div class="text-right">\n                Days: <input type="number" class="qty" name="qty" value="1">\n                  <button data-pid="')
            __M_writer(str( Product.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button>\n                </div>\n            </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/cjpowers/colheritage/homepage/templates/productCatalog.html", "source_encoding": "ascii", "line_map": {"64": 14, "65": 15, "66": 15, "67": 16, "68": 16, "69": 16, "70": 17, "71": 17, "72": 18, "73": 18, "74": 22, "75": 22, "76": 26, "77": 28, "78": 29, "79": 30, "80": 30, "81": 31, "82": 31, "83": 31, "84": 32, "85": 32, "86": 33, "87": 33, "88": 37, "89": 37, "27": 0, "95": 89, "37": 1, "47": 3, "56": 3, "57": 5, "58": 9, "62": 11, "63": 13}, "uri": "productCatalog.html"}
__M_END_METADATA
"""
