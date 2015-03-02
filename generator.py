import sys
import subprocess

from flask import Flask, render_template, url_for, send_from_directory, send_file, render_template_string, Markup
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from flask_frozen import Freezer

#used to render jinja formated text in the body of a post
#will probably remove this and go back to default markdown rendering

#configuration
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT =  'content'
FLATPAGES_HTML_RENDERER = pygmented_markdown
FREEZER_DESTINATION = 'gh-pages'
FREEZER_DESTINATION_IGNORE = ['.git*','.gitignore','CNAME']
FEEZER_RELATIVE_URLS = True
SITE_NAME = 'comicr'
BOOK_DIR = 'books'
PAGE_DIR = 'single_page'
NEWS_DIR = 'news'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.context_processor
def page_types():
    #injects variables for book pages and menu pages, menu pages are used to build main menu links
    menu_pages = (p for p in pages if (p.meta['main-menu']))
    book_page = (p for p in pages if p.meta['type'] == 'book' )
    news_page = (p for p in pages if p.meta['type'] == 'news')
    thumb_nail = latest_comic(book_page, 1)
    return dict(book_page=book_page, menu_pages=menu_pages, news_page=news_page, thumb_nail=thumb_nail)

def total_pages(pages, book):
    #takes a count of pages in the book and returns sum of pages, used for page navigation
    t_pages = (1 for p in pages if p.meta['book'] == book)
    t_pages = sum(t_pages)
    return t_pages

def latest_comic(pages, limit=None):
    #for sorting published pages that are books by latest
    l_comic = (p for p in pages if ((p['type'] == 'book') and 'published'))
    l_comic = sorted(l_comic, reverse=True, key=lambda p: p.meta['published'])
    return l_comic[:limit]

@app.route('/images/<name>')
def images(name):
    if '..' in name or name.startswith('/'):
        abort(404)
    else:
        return send_from_directory('images', name)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

@app.route('/')
def index():
    #take 1 most recent page of published comics
    front_page = latest_comic(pages, 1)
    return render_template('home.html', front_page = front_page)

@app.route('/books/')
def books():
    #finds and lists pages that are chapter: 1 and page_number: 1 in yaml header
    first_page = (p for p in pages if p.meta['chapter'] == 1 and p.meta['page_number'] == 1)
    return render_template('books.html', first_page=first_page, pages=pages)

# @app.route('/archive/')
# def archive():
#     #uses latest_comic to display every published comic page sorted by date
#     all_pages = latest_comic(pages)
#     return render_template('archive.html', all_pages = all_pages)

@app.route('/news/')
def news():
    return render_template('news.html')

# @app.route('/books/<string:book>/')
# def chapter_page(book):
#     #finds and lists pages that chapter 1 in the book string given and are page 1
#     book_page = (p for p in pages if p.meta['book'] == book)
#     chapter_page = (p for p in book_page if p.meta['page_number'] == 1)
#     return render_template('chapter_page.html', chapter_page=chapter_page, book_page=book_page)

@app.route('/<name>.html')
def single_page(name):
    #route for single pages, usually text pages
    path = '{}/{}'.format(PAGE_DIR, name)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/news/<name>.html')
def news_page(name):
    #route for single pages, usually text pages
    path = '{}/{}'.format(NEWS_DIR, name)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/book/<name>.html')
def comic_page(name):
    #variables after 'p' are used to create pagination links within the book stories.
    #these are only passed into the page.html template and work only on 'comic_page' urls
    path = '{}/{}'.format(BOOK_DIR, name)
    p = pages.get_or_404(path)
    t_pages = total_pages(pages, p.meta['book'])
    minus = p.meta['page_number'] - 1
    plus = p.meta['page_number'] + 1
    current_book = p.meta['book']
    current_chapter = p.meta['chapter']
    last_page = (p for p in pages if p.meta['page_number'] == t_pages )
    previous_page = ( p for p in pages if p.meta['page_number'] == minus)
    next_page = ( p for p in pages if p.meta['page_number'] == plus )
    return render_template('comic.html', current_book=current_book,
        current_chapter=current_chapter, p=p, previous_page=previous_page,
        next_page=next_page, t_pages=t_pages, last_page=last_page)

# @app.route('/test/')
# def test():
#     return render_template('test.html', pages=pages)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == "push":
        print ("calling rsync")
        subprocess.check_call(["rsync", "-avc", "--delete", "gh-pages/", "rsyncoutput/"])
    else:
        app.run()
