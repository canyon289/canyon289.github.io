#!/usr/bin/env python

AUTHOR = 'Ravin Kumar'
SITENAME = ['Ravin Kumar']
SITEURL = 'https://ravinkumar.com'
META_DESCRIPTION = 'Ravin Kumar is a small and large model builder and an open source contributor.'

# Content Path
PATH = 'dev/content'

OUTPUT_PATH = 'docs'
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%b %d, %Y"

THEME = "dev/themes/custom"

SUMMARY_MAX_LENGTH = 0

STATIC_PATHS = ['images', 'data', 'js', 'css']

OUTPUT_RETENTION = [".git", "dev", "CNAME"]

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
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ravinakumar'),
          ('github', 'https://github.com/canyon289'),
          ('twitter', 'https://twitter.com/canyon289'),
          ('youtube', 'https://www.youtube.com/channel/UCX78cJQ_6JZVUWw8cj-f0uA/featured'))

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True
PLUGIN_PATHS = ["dev/pelican-plugins"]
PLUGINS = [
    "better_codeblock_line_numbering",
    "pelican_javascript",
    "render_math",
    "simple_footnotes",
    "sitemap",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.8, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
    "exclude": ["tag/", "category/", "author/", "drafts/"],
}


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


MARKDOWN = {
            'extension_configs': {
                'markdown.extensions.codehilite': {'css_class': 'highlight'},
                'markdown.extensions.extra': {},
                'markdown.extensions.toc': {},  # Do not do anchor links {'anchorlink':True}
                'markdown.extensions.meta': {}
                    },
            'output_format': 'html5',
                }

EXTRA_PATH_METADATA = {
    'images/logo/favicon.ico': {'path': 'favicon.ico'}
}

INDEX_SAVE_AS = 'blog.html'
