#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ravin Kumar'
SITENAME = 'Cracking the Data Science Interview'
SITEURL = ''

#Content Path
PATH = 'content'

OUTPUT_PATH = '..'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = "pelican-hyde-modified"

DELETE_OUTPUT_DIRECTORY = True

SUMMARY_MAX_LENGTH = 40

STATIC_PATHS = ['images', 'data', 'js', 'css']

OUTPUT_RETENTION = [".git", "dev"]

GOOGLE_ANALYTICS = 'UA-52706904-2'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["better_codeblock_line_numbering",
           "pelican_javascript",
           "render_math"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = {'markdown.extensions.codehilite' : {'css_class': 'highlight'},
                'markdown.extensions.extra': {},
                'markdown.extensions.meta': {},
                'markdown.extensions.toc': {'anchorlink':True},
                'markdown.extensions.sane_lists':{}}
                
MD_EXTENSIONS = ['fenced_code',
                'codehilite(css_class=highlight, linenums=False)',
                'extra',
                'toc(anchorlink = True)',
                'sane_lists']