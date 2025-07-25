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
	"Apetyt na Świat": "https://www.apetytnaswiat.pl/feed/",
	"Farerskie kadry": "https://farerskiekadry.pl/feed",
	"Farerskie szorty": "https://farerskiekadry.pl/szorty/feed",
	"Finolubna": "https://finolubna.blogspot.com/feeds/posts/default?alt=rss",
	"Føroyar - Wyspy Owcze pod lupą": "https://havnar.blogspot.com/feeds/posts/default?alt=rss",
	# "Fińskie smaki": "https://finskiesmaki.blogspot.com/feeds/posts/default?alt=rss",
	"Gazela w Laponii": "http://gazelawlaponii.pl/feed/",
	"IceStory": "http://icestory.pl/feed/",  # no longer updated
	"Kierunek Norwegia": "https://kieruneknorwegia.pl/feed/",
	"Marchewkowa Skandynawia": "https://www.marchewkowaskandynawia.pl/feed/",
	"NordSide.blog": "https://nordside.blog/feed/",
	"Nordic Talking": "https://nordic-talking.pl/feed/",
	"SKANDIS": "https://blogvigdis.wordpress.com/feed/",
	"Stacja Islandia": "http://www.stacjaislandia.pl/feed/",
	"Szkice Nordyckie": "https://szkicenordyckie.pl/feed/",
	"Szwecjoblog - blog o Szwecji": "https://szwecjoblog.blogspot.com/feeds/posts/default?alt=rss",
	"Szwedzkie Ciekawostki": "https://szwedzkieciekawostki.blogspot.com/feeds/posts/default?alt=rss",
	"Szwedzka półka": "https://www.szwedzkapolka.pl/feed",
	"Utulę Thule": "https://utulethule.pl/feed/",
}

PLANET_TEMPLATE = 'planet.html.tmpl'
PLANET_PAGE = '../docs/index.html'

PLANET_MAX_ARTICLES = 50
PLANET_MAX_ARTICLES_PER_FEED = 5

# set up logging
import logging; logging.basicConfig(level=logging.DEBUG)

for name, url in PLANET_FEEDS.items():
	print('1. [{}]({})'.format(name, url))

