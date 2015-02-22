import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages, pygmented_markdown
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT =  'content'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

def latest_comic(pages, limit=None):
    #for sorting published pages that are books by latest
    l_comic = (p for p in pages if p.meta['book'] and 'published' in p.meta)
    l_comic = sorted(l_comic, reverse=True, key=lambda p: p.meta['published'])
    return l_comic[:limit]

@app.route('/')
def index():
    front_page = latest_comic(pages, 1)
    return render_template('home.html', front_page=front_page)

@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/books/')
def books():
    #finds and lists pages that are chapter: 1 and number: 1 in yaml header
    firstpage = (p for p in pages if p.meta['chapter'] == 1 and p.meta['number'] == 1)
    return render_template('books.html', firstpage=firstpage)

@app.route('/books/<string:book>/')
def chapters(book):
    #finds and lists pages that chapter 1 in the book string given and are page 1
    chapters = (p for p in pages if p.meta['book'] and p.meta['number'] == 1)
    return render_template('books.html', chapters=chapters)

# @app.route('/main-menu/')
# def mainmenu():
#     chapters = (p for p in pages if 'book' in p.meta and p.meta['number'] == 1)
#     firstpage = (p for p in pages if p.meta['chapter'] == 1 and p.meta['number'] == 1)
#     return render_template('_main-menu.html', chapters=chapters, firstpage=firstpage)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
