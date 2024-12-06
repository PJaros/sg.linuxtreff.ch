from pelican.settings import DEFAULT_CONFIG
from pelican.readers import RstReader

config = DEFAULT_CONFIG.copy()

AUTHOR = 'Paul Jaros'
SITENAME = 'Linuxtreff St. Gallen'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'de'

INTRO, _ = RstReader(config).read("content/pages/about.rst")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Ruum42", "https://ruum42.ch"),
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    # ("Ruum42", "https://ruum42.ch"),
    # ("Another social link", "#"),
)

TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

DEFAULT_PAGINATION = False

# From: https://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog
STATIC_PATHS = [
    # 'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    # 'extra/custom.css': {'path': 'custom.css'},
    # 'extra/robots.txt': {'path': 'robots.txt'},
    # 'extra/favicon.png': {'path': 'favicon.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    # 'extra/CNAME': {'path': 'CNAME'},
    # 'extra/LICENSE': {'path': 'LICENSE'},
    # 'extra/README': {'path': 'README'},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = 'foundation-default-colours'
THEME = './themes/sg-linuxtreff-ch-theme'

# FOUNDATION_FOOTER_TEXT = "Linuxtreff St. Gallen"
FOUNDATION_FOOTER_TEXT = ' '