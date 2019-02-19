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
	"Finolubna": "https://finolubna.blogspot.com/feeds/posts/default?alt=rss",
	# "Fińskie smaki": "https://finskiesmaki.blogspot.com/feeds/posts/default?alt=rss",
	"Gazela w Laponii": "http://gazelawlaponii.pl/feed/",
	"Humla": "https://humla.eu/feed/",
	"IceStory": "http://icestory.pl/feed/",
	"Nordic Talking": "https://nordic-talking.pl/feed/",
	"Nowa w Szwecji": "https://www.nowawszwecji.com/blog-feed.xml",
	"Polskie gadanie o szwedzkich rzeczach": "http://polskiegadanieszwedzkierzeczy.pl/feed/",
	"Recenzentka - blog skandynawistki": "http://recenzentka.blox.pl/rss2",
	"SKANDIS": "https://blogvigdis.wordpress.com/feed/",
	"Szwecjoblog - blog o Szwecji": "https://szwecjoblog.blogspot.com/feeds/posts/default?alt=rss",
	"Trolltunga": "https://www.trolltunga-norweski.com/feed.xml",
	"Utulę Thule": "https://utulethule.wordpress.com/feed/",
	"poFIKAsz?": "https://pofikasz.pl/feed/",
}

PLANET_TEMPLATE = 'planet.html.tmpl'
PLANET_PAGE = '../docs/index.html'

PLANET_MAX_ARTICLES = 50
PLANET_MAX_ARTICLES_PER_FEED = 5

# set up logging
import logging; logging.basicConfig(level=logging.DEBUG)

for name, url in PLANET_FEEDS.items():
	print('1. [{}]({})'.format(name, url))

