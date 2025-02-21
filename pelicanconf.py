AUTHOR = 'mrJungle'
SITENAME = 'Super Competitive Arena dev BLOG'
SITEURL = "http://localhost:8000"

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

ARTICLE_ORDER_BY = 'date'


MENUITEMS = (
    ('Home', SITEURL),  # Link alla home
    ('Blog', f'{SITEURL}/'),  # Altro link, se necessario
#    ('Chi siamo', f'{SITEURL}/about/'),  # Link a una pagina statica
)



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 7
USE_FOLDER_AS_CATEGORY = True  # Opzionale, ma utile
# In pelicanconf.py

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#THEME = "themes/sca"
#THEME = "themes/pelican-blue-master"
THEME = "themes/scustom"

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

AVATAR = "/theme/images/logo.png"

# Correggi i percorsi statici
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

OUTPUT_PATH = "docs/"

