#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nordic Talking'
SITENAME = 'Nordycka Planeta'
SITEURL = ''

PATH = '../docs'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
	('Pelican', 'http://getpelican.com/'),
	('Nordic Talking', 'https://nordic-talking.pl/'),
)

# Social widget
SOCIAL = (
	('Festiwal Nordic Talking', 'https://www.facebook.com/nordictalkingfestival/'),
)

DEFAULT_PAGINATION = 10

# RSS planet
PLUGINS = [
	'pelican_planet',
]

# https://pypi.org/project/pelican-planet/
PLANET_FEEDS = {
	"Farerskie kadry": "https://farerskiekadry.pl/feed",
	"IceStory": "http://icestory.pl/feed/",
	"Nordic Talking": "https://nordic-talking.pl/feed/",
	"SKANDIS": "https://blogvigdis.wordpress.com/feed/",
	"Utulę Thule": "https://utulethule.wordpress.com/feed/",
	"poFIKAsz?": "https://pofikasz.pl/feed/",
}

PLANET_TEMPLATE = 'planet.html.tmpl'
PLANET_PAGE = '../docs/index.html'

PLANET_MAX_ARTICLES = 50
PLANET_MAX_ARTICLES_PER_FEED = 5

# Polish dates

# On Unix/Linux
DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
    'pl': ('pl_PL.utf8','%m %d %Y'),
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
