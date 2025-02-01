# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1738394054.5773232
_enable_loop = True
_template_filename = 'themes/reveal/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'belowtitle', 'sourcelink', 'content', 'custom_reveal', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('reveal', context._clean_inheritance_tokens(), templateuri='reveal_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'reveal')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'reveal')._populate(_import_ns, ['*'])
        def content():
            return render_content(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        def custom_reveal():
            return render_custom_reveal(context._locals(__M_locals))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        reveal = _mako_get_namespace(context, 'reveal')
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        __M_writer(str(reveal.html_reveal_head()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n\n<!-- Menubar -->\n\n<div class="navbar navbar-fixed-top" id="navbar" style="font-family: Open Sans;">\n    <div class="navbar-inner">\n        <div class="container">\n\n        <!-- .btn-navbar is used as the toggle for collapsed navbar content -->\n        <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n        </a>\n\n            <a class="brand" href="')
        __M_writer(str(abs_link('/')))
        __M_writer('">\n')
        if logo_url:
            __M_writer('                <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(str(blog_title))
            __M_writer('" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('                <span id="blog-title">')
            __M_writer(str(blog_title))
            __M_writer('</span>\n')
        __M_writer('            </a>\n            <!-- Everything you want hidden at 940px or less, place within here -->\n            <div class="nav-collapse collapse">\n                <ul class="nav">\n                    ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\n                    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n                </ul>\n')
        if search_form:
            __M_writer('                    ')
            __M_writer(str(search_form))
            __M_writer('\n')
        __M_writer('                <ul class="nav pull-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n')
        if show_sourcelink:
            __M_writer('                    <li>')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer('</li>\n')
        __M_writer('                ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n                </ul>\n            </div>\n        </div>\n    </div>\n</div>\n<!-- End of Menubar -->\n\n<div class="reveal"><div class="slides">\n    <section>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n    </section>\n</div></div>\n\n')
        __M_writer(str(reveal.html_reveal_body()))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'custom_reveal'):
            context['self'].custom_reveal(**pageargs)
        

        __M_writer('\n\n<div class="navbar navbar-fixed-bottom" style="font-family: Open Sans;">\n    <div class="navbar-inner">\n        <div class="footerbox">\n            ')
        __M_writer(str(content_footer))
        __M_writer('\n        </div>\n    </div>\n</div>\n\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <script type="text/javascript">jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});\n    $(window).on(\'hashchange\', function(){\n        if (location.hash && $(location.hash)[0]) {\n            $(\'body\').animate({scrollTop: $(location.hash).offset().top - $(\'#navbar\').outerHeight(true)*1.2 }, 1);\n        }\n    });\n    $(document).ready(function(){$(window).trigger(\'hashchange\')});\n    </script>\n   ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n   ')
        __M_writer(str(body_end))
        __M_writer('\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'reveal')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'reveal')._populate(_import_ns, ['*'])
        def belowtitle():
            return render_belowtitle(context)
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('                    <li>')
            __M_writer(str(base.html_translations()))
            __M_writer('</li>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'reveal')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'reveal')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_custom_reveal(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'reveal')._populate(_import_ns, ['*'])
        def custom_reveal():
            return render_custom_reveal(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'reveal')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/reveal/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "64": 2, "65": 3, "66": 4, "67": 4, "68": 5, "69": 5, "70": 6, "71": 6, "76": 9, "77": 10, "78": 10, "79": 27, "80": 27, "81": 28, "82": 29, "83": 29, "84": 29, "85": 29, "86": 29, "87": 31, "88": 32, "89": 33, "90": 33, "91": 33, "92": 35, "93": 39, "94": 39, "95": 40, "96": 40, "97": 42, "98": 43, "99": 43, "100": 43, "101": 45, "106": 50, "107": 51, "108": 52, "113": 52, "114": 54, "115": 54, "116": 54, "121": 64, "122": 68, "123": 68, "128": 70, "129": 75, "130": 75, "131": 80, "132": 80, "137": 89, "138": 90, "139": 90, "145": 7, "154": 7, "160": 46, "172": 46, "173": 47, "174": 48, "175": 48, "176": 48, "177": 50, "183": 52, "197": 64, "211": 70, "225": 89, "239": 225}}
__M_END_METADATA
"""
