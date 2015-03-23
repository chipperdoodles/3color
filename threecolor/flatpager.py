import sys
import subprocess
import os.path as op

from werkzeug.contrib.atom import AtomFeed
from flask import Flask, render_template, url_for, send_from_directory, send_file
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs

from threecolor import app

pages = FlatPages()

@app.context_processor
def page_types():
    #injects variables for book pages and menu pages, menu pages are used to build main menu links
    menu_pages = (p for p in pages if (p.meta['menu']))
    book_page = (p for p in pages if p.meta['page_type'] == 'book' )
    news_page = (p for p in pages if p.meta['page_type'] == 'news')
    thumb_nail = latest_comic(book_page, app.config['THUMB_STORY'], 1)
    return dict(book_page=book_page, menu_pages=menu_pages, news_page=news_page, thumb_nail=thumb_nail)

def total_pages(pages, book):
    #takes a count of pages in the book and returns sum of pages, used for page navigation
    t_pages = (1 for p in pages if p.meta['book'] == book)
    t_pages = sum(t_pages)
    return t_pages

def latest_comic(pages, book, limit=None):
    #for sorting published pages that are books by latest
    l_comic = (p for p in pages if ((p['page_type'] == 'book') and p['book'] == book))
    l_comic = sorted(l_comic, reverse=True, key=lambda p: p.meta['published'])
    return l_comic[:limit]

@app.route('/images/<name>')
def images(name):

    path = app.config['IMAGE_DIR']

    if '..' in name or name.startswith('/'):
        abort(404)
    else:
        return send_from_directory(path, name)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('friendly'), 200, {'Content-Type': 'text/css'}

@app.route('/')
def index():
    #take 1 most recent page of published comics
    front_page = latest_comic(pages, app.config['MAIN_STORY'], 1)
    return render_template('home.html', front_page = front_page)

@app.route('/books/')
def books():
    #finds and lists pages that are chapter: 1 and page_number: 1 in yaml header
    first_page = (p for p in pages if p.meta['chapter'] == 1 and p.meta['page_number'] == 1)
    return render_template('books.html', first_page=first_page, pages=pages)

@app.route('/news/')
def news():
    return render_template('news.html')

@app.route('/atom.xml')
#atom feed, only works with a patch to werkzeug/contrip/atom.py file will look into more
#https://github.com/mitsuhiko/werkzeug/issues/695
def atom_feed():
    feed = AtomFeed('Feed for '+app.config['SITE_NAME'], feed_url=app.config['DOMAIN']+url_for('atom_feed'), url=app.config['DOMAIN'])
    comic_feed = (p for p in pages if p.meta['page_type'] != 'single_page')
    for p in comic_feed:
        feed.add(p.meta['title'],
                content_type='html',
                url=app.config['DOMAIN']+p.path+'.html',
                updated=p.meta['published'],
                summary=p.body)
    return feed.get_response()

@app.route('/<name>.html')
def single_page(name):
    #route for single pages, usually text pages
    path = '{}/{}'.format(app.config['PAGE_DIR'], name)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/news/<name>.html')
def news_page(name):
    #route for single pages, usually text pages
    path = '{}/{}'.format(app.config['NEWS_DIR'], name)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/books/<name>.html')
def comic_page(name):
    #variables after 'p' are used to create pagination links within the book stories.
    #these are only passed into the page.html template and work only on 'comic_page' urls
    path = '{}/{}'.format(app.config['BOOK_DIR'], name)
    p = pages.get_or_404(path)
    t_pages = total_pages(pages, p.meta['book'])
    minus = p.meta['page_number'] - 1
    plus = p.meta['page_number'] + 1
    current_book = p.meta['book']
    current_chapter = p.meta['chapter']
    first_page = (p for p in pages if p.meta['page_number'] ==1 and p.meta['book'] == current_book)
    last_page = (p for p in pages if p.meta['page_number'] == t_pages)
    previous_page = ( p for p in pages if p.meta['page_number'] == minus)
    next_page = ( p for p in pages if p.meta['page_number'] == plus )
    return render_template('comic.html', current_book=current_book,
        current_chapter=current_chapter, p=p, previous_page=previous_page,
        next_page=next_page, t_pages=t_pages, last_page=last_page, first_page=first_page)
