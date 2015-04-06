# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428163568.450612
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/shoppingCart.html'
_template_uri = 'shoppingCart.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        current_cart = context.get('current_cart', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        current_cart = context.get('current_cart', UNDEFINED)
        def content():
            return render_content(context)
        int = context.get('int', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<table class="table table-striped table-bordered">\n\t<tr>\n\t\t<th>Product Name</th>\n\t\t<th>Quantity</th>\n\t\t<th>Price</th>\n\t\t<th>Subtotal</th>\n\t\t<th>Action</th>\n\t</tr>\n\n\n\t')
        grand_total = 0
        
        __M_writer('\n\n')
        for product, value in current_cart.items():
            __M_writer('\t\t')

            price = int(value[0].currentPrice)
            qty = value[1]
            sub_total = (price * qty)
            grand_total += sub_total
                            
            
            __M_writer('\n\t\t<tr>\n\t\t\t<td>')
            __M_writer(str( value[0].name ))
            __M_writer('</td>\n\t\t\t<td>')
            __M_writer(str( value[1] ))
            __M_writer('</td>\n\t\t\t<td>')
            __M_writer(str( value[0].currentPrice ))
            __M_writer('</td>\n\t\t\t<td>')
            __M_writer(str( sub_total ))
            __M_writer('</td>\n\t\t\t<td><button data-pid="')
            __M_writer(str( value[0].id ))
            __M_writer('" class="deleteCartItem btn btn-danger btn-xs">Remove Cart Item</button></td>\n\t\t</tr>\n')
        __M_writer('\t\t<tr>\n\t\t\t<td>Total:</td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td>')
        __M_writer(str( grand_total ))
        __M_writer('</td>\n\t\t\t<td></td>\n\t\t</tr>\n</table>\n\n')
        __M_writer(str('Please Login to Check Out' if request.user.username == "" else '<a href="/homepage/shoppingCart.checkout/"><button id="checkoutButton" class="btn btn-primary">Check Out!</button></a>' ))
        __M_writer('\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "shoppingCart.html", "source_encoding": "ascii", "line_map": {"70": 22, "71": 24, "72": 24, "73": 25, "74": 25, "75": 26, "76": 26, "77": 27, "78": 27, "79": 28, "80": 28, "81": 31, "82": 35, "83": 35, "84": 40, "85": 40, "27": 0, "91": 85, "37": 1, "42": 45, "48": 3, "57": 3, "58": 14, "60": 14, "61": 16, "62": 17, "63": 17}, "filename": "/Users/cjpowers/colheritage/homepage/templates/shoppingCart.html"}
__M_END_METADATA
"""
