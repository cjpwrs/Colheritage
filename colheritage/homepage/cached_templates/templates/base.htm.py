# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428164328.267
_enable_loop = True
_template_filename = '/Users/cjpowers/colheritage/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n\n  <meta name="description" content="The colonial heritage foundation is a foundation whose main goal is to enrich the american people with the great history of this county">\n  <meta name="keywords" content="colonial, heritage, foundation, festival, fun, free, Utah">\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>Colonial Heritage Foundation</title>\n    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <!-- Latest compiled and minified CSS -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n\n    <!-- Optional theme -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css">\n\n    <!-- Latest compiled and minified JavaScript -->\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n\n    <link rel="icon" type="image/ico" href="/static/homepage/media/favicon.ico">\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n\n    <header>\n      <div id="headerImage"><img src="/static/homepage/media/Meet_history.jpg" class="img-responsive" alt="Responsive image"></div>\n      <div class="headerTitle"> The Colonial Heritage Foundation<div id="subHeaderTitle"><h4>"Meet History Face to Face"</h4></div></div>\n      <div id="login">\n\n        <div class="pull-right">\n')
        if request.user.is_authenticated():
            __M_writer('            Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer('\n            <a href="http://localhost:8000/homepage/logout"><button type="button" class="btn btn-default"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> Logout</button></a>\n')
        else:
            __M_writer('            <button id="show_login_dialog" class="btn btn-success">Login Here</button>\n')
        __M_writer('        </div>\n\n    </header>\n  \n\n  <div class="row">\n    <div class="col-md-2" id="sideBar">\n      <p><a href="/homepage/index/" id="sideBar">Home</a><span class="glyphicon glyphicon-home" aria-hidden="true"></span></p>\n      <p><a href="/homepage/events.upcoming/" id="sideBar">Upcoming Events</a>\n      <p><a href="/homepage/productCatalog/" id="sideBar">Store</a>\n      <p><a href="/homepage/adminCrud/" id="sideBar">Admin Pages</a>\n\n    </div>\n    <div class="col-md-8">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(' \n    </div>\n  </div>\n\n\n\n  <footer>\n    CJ Powers - Group 2-4\n  </footer>\n\n\n  \n\n\n\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n        Site content goes here in sub-templates.\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"69": 65, "75": 69, "16": 4, "18": 0, "28": 2, "29": 4, "30": 5, "34": 5, "35": 18, "36": 22, "37": 22, "38": 23, "39": 23, "40": 34, "41": 34, "42": 34, "43": 45, "44": 46, "45": 46, "46": 46, "47": 48, "48": 49, "49": 51, "54": 67, "55": 84, "56": 84, "57": 84, "63": 65}, "source_encoding": "ascii", "filename": "/Users/cjpowers/colheritage/homepage/templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
