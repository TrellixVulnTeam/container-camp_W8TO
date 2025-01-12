# Version 2.0, May 2020
# -*- coding: utf-8 -*-

import sys
import os
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

extensions = [
    'sphinx.ext.autodoc',
]

project = 'YOUR PROJECT NAME HERE as topic_quick_start'
copyright = '2020, CyVerse'
author = 'CyVerse'
version = '2.0'
release = '2.0'

language = None
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst']

common_static_path = os.path.join(os.path.dirname(__file__), 'static')

templates_path = ['_templates']
html_static_path = ['_static', common_static_path]
exclude_patterns = ['_build']
master_doc = 'index'
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'

htmlhelp_basename = 'CyVerse_Documentation'

latex_elements = {}
latex_documents = [
    (master_doc, 'CyVerseDocumentation.tex', 'CyVerse Documentation',
     'CyVerse', 'manual'),
]

man_pages = [
    (master_doc, 'CyVerse Documentation', 'CyVerse Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'CyVerse Documentation', 'CyVerse Documentation',
     author, 'CyVerse', 'CyVerse',
     'Miscellaneous'),
]

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']


def setup(app):
    app.add_config_value(
        'recommonmark_config',
        {
            'enable_auto_toc_tree': True,
            'enable_eval_rst': True,
            'auto_toc_tree_section': 'Contents',
        },
        True
    )
    app.add_transform(AutoStructify)
    app.add_css_file('cyverse.css')
    app.add_css_file('detail-expand.css')
    app.add_css_file('question-answer.css')
    #uncomment to enable table sorting app.add_js_file('jquery.tablesorter.min.js')
    app.add_js_file('cyverse.js')
    app.add_js_file('detail-expand.js')
    app.add_js_file('question-answer.js')
    app.add_js_file('intercom-script-for-learning.js')
