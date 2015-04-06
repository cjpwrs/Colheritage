# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425752313.608545
_enable_loop = True
_template_filename = '/Users/jeffreymccraney/test_dmp/homepage/templates/details.html'
_template_uri = 'details.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
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
        def content():
            return render_content(context)
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t<br>\n    \t\t<div class="imageCenter"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/product_images/')
        __M_writer(str( product.name))
        __M_writer('.jpg/" /></div>\n\t    \t<div class="text-muted text-center">')
        __M_writer(str( product.name ))
        __M_writer('</div>\n\t    \t<div class="text-muted text-center">Description: ')
        __M_writer(str( product.description ))
        __M_writer('</div>\n\t    \t<div class="text-muted text-center">Price: $')
        __M_writer(str( product.currentPrice ))
        __M_writer('</div>\n            <div class= "text-center">Qty: <input type="number" id="qty" name="qty"></div>\n            <br>\n    \t\t<div class="text-center">\n    \t\t\t<button data-pid="')
        __M_writer(str( product.id ))
        __M_writer('" class="add_button btn btn-xs btn-warning">Add to Cart</button>\n    \t\t\t<br>\n    \t\t\t<br>\n    \t\t\t<a href="/homepage/productCatalog"><button class="add_button btn btn-primary">Return to Product Page!</button></a>\n    \t\t</div>\n\n    \t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jeffreymccraney/test_dmp/homepage/templates/details.html", "uri": "details.html", "line_map": {"64": 8, "65": 12, "66": 12, "27": 0, "36": 1, "72": 66, "46": 3, "54": 3, "55": 5, "56": 5, "57": 5, "58": 5, "59": 6, "60": 6, "61": 7, "62": 7, "63": 8}, "source_encoding": "ascii"}
__M_END_METADATA
"""
