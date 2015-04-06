# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428209251.641228
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/artisanCatalog.html'
_template_uri = 'artisanCatalog.html'
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('    <title>Artisan Products</title>\n    <h1>Artisan Products</h1>\n    <br>\n    <div class="text-right">\n        Search Products: <input type="search" id="searchProducts">\n    </div>\n    ')


    

        __M_writer('\n')
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
            __M_writer('</div>\n    \t</a>\n\n    \t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 16, "65": 17, "66": 17, "67": 17, "36": 1, "69": 18, "70": 19, "71": 19, "77": 71, "46": 3, "54": 3, "55": 5, "56": 11, "68": 18, "27": 0, "60": 13, "61": 14, "62": 15, "63": 16}, "uri": "artisanCatalog.html", "filename": "/Users/cjpowers/colheritage/homepage/templates/artisanCatalog.html"}
__M_END_METADATA
"""
