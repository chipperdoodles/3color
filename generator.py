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

# navigation variables
# minus = (p for p in pages if page['page_number'] - 1)
# plus = p.meta['page_number'] + 1
# current_book = p.meta['book']
# current_chapter = p.meta['chapter']
# previous_page = ( p for p in pages if p.meta['page_number'] == minus)
# next_page = ( p for p in pages if p.meta['page_number'] == plus )

def latest_comic(pages, limit=None):
    #for sorting published pages that are books by latest
    l_comic = (p for p in pages if p.meta['book'] and 'published' in p.meta)
    l_comic = sorted(l_comic, reverse=True, key=lambda p: p.meta['published'])
    return l_comic[:limit]

def total_pages(pages, book):
    t_pages = (1 for p in pages if p.meta['book'] == book)
    t_pages = sum(t_pages)
    return t_pages

@app.route('/')
def index():
    #take 1 most recent page of comics
    front_page = latest_comic(pages, 1)
    return render_template('home.html', front_page=front_page)

@app.route('/books/')
def books():
    #finds and lists pages that are chapter: 1 and page_number: 1 in yaml header
    book_page = (p for p in pages if p.meta['book'])
    first_page = (p for p in pages if p.meta['chapter'] == 1 and p.meta['page_number'] == 1)
    return render_template('books.html', book_page=book_page, first_page=first_page)

# @app.route('/books/<string:book>/')
# def chapter_page(book):
#     #finds and lists pages that chapter 1 in the book string given and are page 1
#     book_page = (p for p in pages if p.meta['book'] == book)
#     chapter_page = (p for p in book_page if p.meta['page_number'] == 1)
#     return render_template('chapter_page.html', chapter_page=chapter_page, book_page=book_page)

# @app.route()
# def single_page():


@app.route('/<path:path>.html')
def comic_page(path):
    #messy, trying to see if i could get pagination on page for back and next pages in a current chapter
    page = pages.get_or_404(path)
    t_pages = total_pages(pages, page.meta['book'])
    minus = page.meta['page_number'] - 1
    plus = page.meta['page_number'] + 1
    current_book = page.meta['book']
    current_chapter = page.meta['chapter']
    book_page = (p for p in pages if p.meta['book'])
    last_page = (p for p in pages if p.meta['page_number'] == t_pages )
    previous_page = ( p for p in pages if p.meta['page_number'] == minus)
    next_page = ( p for p in pages if p.meta['page_number'] == plus )
    return render_template('page.html', current_book=current_book, current_chapter=current_chapter, book_page=book_page,
     page=page, previous_page=previous_page, next_page=next_page, t_pages=t_pages, last_page=last_page)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
