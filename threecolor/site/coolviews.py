import os

from ..configs import config

from flask import abort, current_app, Blueprint, render_template, send_from_directory, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer

from werkzeug.contrib.atom import AtomFeed


freezer = Freezer()
pages = FlatPages()
cfg = config.make_usr_cfg()

site = Blueprint('site', __name__,
                 url_prefix='',
                 template_folder=cfg['TEMPLATES'],
                 static_folder=cfg['STATIC'],
                 static_url_path='/static/site'
                 )


@site.context_processor
def page_types():

    """
    injects variables for book pages and main-menu

    """

    main_menu = (p for p in pages if 'main-menu' in p['menu']['menuname'])
    book_pages = (p for p in pages if 'book' == p['page_type'])
    news_pages = (p for p in pages if 'news' == p['page_type'])
    gallery_items = (p for p in pages if 'gallery' == p['page_type'])
    thumb_nail = latest_comic(book_pages, current_app.config['THUMB_STORY'], 1)
    # FIXME: uses same name as book_list function below
    # book_list = (p['page_type'] for p in pages)
    return {
        "book_page": book_pages,
        "main_menu": main_menu,
        "news_page": news_pages,
        "thumb_nail": thumb_nail,
        "book_list": book_list,
        "pages": pages
    }


def total_pages(pages, book):
    # takes a count of pages in the book and returns sum of pages, used for page navigation
    t_pages = (1 for p in pages if p.meta['book'] == book)
    t_pages = sum(t_pages)
    return t_pages


def latest_comic(pages, book, limit=None):
    # for sorting published pages that are books in the main story by latest
    l_comic = (p for p in pages if p['book']['title'] == book and p['page_type'] == 'book')
    l_comic = sorted(l_comic, reverse=True, key=lambda p: p.meta['published'])
    return l_comic[:limit]


def page_feed(pages, limit=None):
    # for sorting published pages that are books by latest
    l_comic = (p for p in pages if p['page_type'] == 'book')
    l_comic = sorted(l_comic, reverse=True, key=lambda p: p.meta['published'])
    return l_comic[:limit]


def book_list():
    # returns a list of the book titles in book type
    first_page = (p for p in pages if p['book']['chapter'] == 1 and p['book']['page_number'] == 1)
    book_titles = [p['book']['title'] for p in first_page]
    return book_titles


@site.route('/images/<subdir>/<name>')
def images(subdir, name):

    """
    static image file delivery.
    This serves image files from the project
    """

    path = os.path.join(current_app.config['IMAGE_DIR'], subdir)

    if '..' in name or name.startswith('/'):
        abort(404)
    else:
        return send_from_directory(path, name)


# FIXME: this probably breaks with the new image subdirectories, fix this!
@freezer.register_generator
def images_url_generator():

    """
    For flask_frozen to make sure images in the instance/images folder
    get built into the static html output.
    """

    path = os.listdir(current_app.config['IMAGE_DIR'])

    for f in path:
        yield '/images/'+f


@site.route('/')
def index():

    """
    Renders a template for the home page that displays the most recent
    published comic in the main story line.
    """
    front_page = latest_comic(pages, current_app.config['MAIN_STORY'], 1)
    return render_template('home.html', front_page=front_page)


@site.route('/books/')
def books():

    """
    Finds and lists pages that are chapter: 1 and page_number: 1 in yaml header
    """

    first_page = (p for p in pages if p['book']['chapter'] == 1 and p['book']['page_number'] == 1)
    return render_template('books.html', first_page=first_page)


@site.route('/news/')
def news():

    """
    Renders the news template, this page is a feed of news posts.
    """

    return render_template('news.html')


@site.route('/gallery/')
def gallery():
    """
    Renders gallery page
    """

    return render_template('gallery.html')

@site.route('/atom.xml')
def atom_feed():

    """
    Uses the werkzeug contrib.atom module to generate atom feed
    """

    feed = AtomFeed('Feed for '+current_app.config['SITE_NAME'],
                    feed_url=current_app.config['DOMAIN']+url_for('.atom_feed'),
                    url=current_app.config['DOMAIN'])
    # comic_feed = (p for p in pages if p.meta['page_type'] != 'single_page')
    comic_feed = page_feed(pages, 10)
    for p in comic_feed:
        feed.add(p.meta['title'],
                 content_type='html',
                 url=current_app.config['DOMAIN']+p.path+'.html',
                 published=p.meta['published'],
                 updated=p.meta['modified'],
                 summary=p.body)
    return feed.get_response()


@site.route('/<name>.html')
def single_page(name):

    """
    Route for custom pages, usually text pages such as about me or f.a.q's
    """
    path = '{}/{}'.format(current_app.config['PAGE_DIR'], name)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@site.route('/news/<name>.html')
def news_page(name):
    """
    route for news post pages
    """
    path = '{}/{}'.format(current_app.config['NEWS_DIR'], name)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@site.route('/<book>/c<int:chapter>/p<int:number>/<name>.html')
def comic_page(book, chapter, number, name):
    """
    variables after 'p' are used to create pagination links within book stories.
    These are only passed into the page.html template and only work on
    'comic_page' urls
    """
    path = '{}/{}'.format(current_app.config['BOOK_DIR'], name)
    p = pages.get_or_404(path)
    t_pages = total_pages(pages, p['book']['title'])
    minus = p['book']['page_number'] - 1
    plus = p['book']['page_number'] + 1
    current_book = p['book']['title']
    current_chapter = p.meta['book']['chapter']
    first_page = (p for p in pages if p['book']['page_number'] == 1 and p['book']['title'] == current_book)
    last_page = (p for p in pages if p['book']['page_number'] == t_pages)
    previous_page = (p for p in pages if p['book']['page_number'] == minus)
    next_page = (p for p in pages if p['book']['page_number'] == plus)
    return render_template(
        'comic.html',
        current_book=current_book,
        current_chapter=current_chapter,
        p=p,
        previous_page=previous_page,
        next_page=next_page,
        t_pages=t_pages,
        last_page=last_page,
        first_page=first_page
    )


def chill():
    # function to build the site into static files
    freezer.freeze()
