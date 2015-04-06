# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425756208.003051
_enable_loop = True
_template_filename = '/Users/jeffreymccraney/test_dmp/homepage/templates/shopping.Cart.html'
_template_uri = 'shopping.Cart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<table class="table table-striped table-bordered">\n\t\t\t<tr>\n\t\t\t\t<th>Product Name</th>\n\t\t\t\t<th>Quantity</th>\n\t\t\t\t<th>Price</th>\n\t\t\t\t<th>Subtotal</th>\n\t\t\t</tr>\n\t\t\n\t</table>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jeffreymccraney/test_dmp/homepage/templates/shopping.Cart.html", "uri": "shopping.Cart.html", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii"}
__M_END_METADATA
"""
