AUTHOR = 'Paul Jaros'
SITENAME = 'Linuxtreff St. Gallen'
SITEURL = ''

# From: https://stackoverflow.com/a/23724453/406423
# Funktioniert seit Pelican 4.2 nicht mehr
#
# SITEURL = '/blog'
# OUTPUT_PATH = 'output/blog'
# PAGE_URL = '../{slug}.html'
# PAGE_SAVE_AS = '../{slug}.html'
# DISPLAY_PAGES_ON_MENU = False
# DISPLAY_CATEGORIES_ON_MENU = False
# MENUITEMS = [('Home', '/'), ('Blog', '/blog/')]

# From https://stackoverflow.com/a/59508010/406423
ARTICLE_URL = "blog/{date:%Y}-{date:%m}-{date:%d}-{slug}.html"
ARTICLE_SAVE_AS = "blog/{date:%Y}-{date:%m}-{date:%d}-{slug}.html"
INDEX_SAVE_AS = "blog/index.html"

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'de'

# From: https://stackoverflow.com/a/64725173/406423
# Inhalt auf Hauptseite hinzufügen - vielleicht für später hier auskommentiert
# from pelican.settings import DEFAULT_CONFIG
# from pelican.readers import RstReader
# config = DEFAULT_CONFIG.copy()
# INTRO, _ = RstReader(config).read("content/pages/about.rst")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Linked neighborhood
LINKS = (
      ("Ruum42",                 "https://ruum42.ch")
    , ("Linuxtreff Kreuzlingen", "https://kreuzlingen.linuxtreff.ch")
)

TAGS_SAVE_AS = ''
# CATEGORY_SAVE_AS = ''

DEFAULT_PAGINATION = False

# From: https://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog
STATIC_PATHS = [
    # 'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/ice.jpg': {'path': 'ice.jpg'},
    'extra/tux-sg.png': {'path': 'tux-sg.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = 'foundation-default-colours'
THEME = './themes/sg-linuxtreff-ch-theme'

# FOUNDATION_FOOTER_TEXT = "Linuxtreff St. Gallen"
FOUNDATION_FOOTER_TEXT = ' '

# 'markdown.extensions.attr_list' is allready included by default
# This left here as a reminder how to add or reconfigure python-markdown plugins
# MARKDOWN = {'extension_configs': {
#         'markdown.extensions.attr_list':{},
#     },
# }