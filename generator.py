import sys
import math

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
    #take 1 most recent page of comics
    front_page = latest_comic(pages, 1)
    return render_template('home.html', front_page=front_page)

@app.route('/books/')
def books():
    #finds and lists pages that are chapter: 1 and number: 1 in yaml header
    bookpages = (p for p in pages if p.meta['book'])
    firstpage = (p for p in pages if p.meta['chapter'] == 1 and p.meta['number'] == 1)
    return render_template('books.html', bookpages=bookpages, firstpage=firstpage)

@app.route('/books/<string:book>/')
def chapters(book):
    #finds and lists pages that chapter 1 in the book string given and are page 1
    bookpages = (p for p in pages if p.meta['book'] == book)
    chapters = (p for p in bookpages if p.meta['number'] == 1)
    return render_template('chapters.html', chapters=chapters, bookpages=bookpages)

@app.route('/<path:path>/')
def page(path):
    #messy, trying to see if i could get pagination on page for back and next pages in a current chapter
    page = pages.get_or_404(path)
    minus = page.meta['number'] - 1
    plus = page.meta['number'] + 1
    currentbook = page.meta['book']
    currentchapter = page.meta['chapter']
    previouspage = ( p for p in pages if p.meta['number'] == minus)
    nextpage = ( p for p in pages if p.meta['number'] == plus )
    return render_template('page.html', currentbook=currentbook, currentchapter=currentchapter, page=page, previouspage=previouspage, nextpage=nextpage)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
