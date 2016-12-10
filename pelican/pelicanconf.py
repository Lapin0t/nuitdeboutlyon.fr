#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nuit Debout Lyon'
SITENAME = 'Nuit Debout Lyon'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['uploads']


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr-FR'
LOCALE = 'fr-FR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [('Forum', 'https://forum.nuitdeboutlyon.fr/'),
         ('Facebook', 'https://www.facebook.com/NuitDeboutLyon'),
         ('Twitter', 'https://twitter.com/NuitDeboutLyon'),
         ('Instagram', 'https://www.instagram.com/nuitdeboutlyon/')]

# Social widget
# TODO: le thème ne supporte pas ça
SOCIAL = (('Facebook', 'https://www.facebook.com/NuitDeboutLyon'),
          ('Twitter', 'https://twitter.com/NuitDeboutLyon'),
          ('Instagram', 'https://www.instagram.com/nuitdeboutlyon/'))

GITHUB_URL = 'https://github.com/Lapin0t/nuitdeboutlyon.fr'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme-medius'

MD_EXTENTIONS = ['extra', 'smarty', 'sane_lists', 'headerid']
TYPOGRIFY = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['events']


PLUGIN_EVENTS = {'ics_fname': 'calendar.ics'}

