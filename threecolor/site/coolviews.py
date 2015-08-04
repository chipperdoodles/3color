import os

from ..configs import config

from flask import abort, current_app, Blueprint, render_template, send_from_directory, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer, walk_directory

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

# helper functions
@site.context_processor
def page_types():

    """
    injects variables for book pages and main-menu

    """

    main_menu = (mp for mp in pages if 'main-menu' in mp['menu']['menuname'])
    book_pages = (bp for bp in pages if 'book' == bp['page_type'])
    news_pages = (np for np in pages if 'news' == np['page_type'])
    gallery_items = (gp for gp in pages if 'gallery' == gp['page_type'])
    thumb_nail = latest_comic(book_pages, current_app.config['THUMB_STORY'], 1)
    # FIXME: uses same name as book_list function below
    # book_list = (p['page_type'] for p in pages)
    return {
        "book_page": book_pages,
        "main_menu": main_menu,
        "news_page": news_pages,
        "thumb_nail": thumb_nail,
        "book_list": book_list,
        "pages": pages,
        "gallery_items": gallery_items
    }


def total_pages(pages, book):
    # takes a count of pages in the book and returns sum of pages, used for page navigation
    t_pages = (1 for p in pages if p.meta['book']['title'] == book)
    t_pages = sum(t_pages)
    return t_pages


def first_last(pages, book, which):

    """
    Used to determin the first and last page number of a story
    """

    b_pages = (bp for bp in pages if bp.meta['book']['title'] == book)
    pnum_list = [bnum.meta['book']['page_number'] for bnum in b_pages]
    first_pnum = min(pnum_list)
    last_pnum = max(pnum_list)
    if which == 'fnum':
        return first_pnum
    elif which == 'lnum':
        return last_pnum
    else:
        print('No min or max selected')

def latest_comic(pages, book, limit=None):

    """
    Sorts comics by most recently published
    """

    l_comic = (p for p in pages if p['book']['title'] == book and p['page_type'] == 'book')
    l_comic = sorted(l_comic, reverse=True, key=lambda p: p.meta['published'])
    return l_comic[:limit]


def page_feed(pages, limit=None):

    """
    Used to sort comics specifically for atom feed
    """

    l_comic = (p for p in pages if p['page_type'] == 'book')
    l_comic = sorted(l_comic, reverse=True, key=lambda p: p.meta['published'])
    return l_comic[:limit]


def book_list():

    """
    Currently unused, presents a list of the different book titles
    """

    first_page = (p for p in pages if p['book']['chapter'] == 1 and p['book']['page_number'] == 1)
    book_titles = [p['book']['title'] for p in first_page]
    return book_titles


def feed_helper(cf):

    """
    Helper function for the atom feed to name entries
    """

    if cf.meta['page_type'] is 'book':

        if cf.meta['title'] is '':
            ptitle = cf.meta['book']['title']+' '+str(cf.meta['book']['page_number'])
        else:
            ptitle = cf.meta['title']

    else:

        if cf.meta['title'] is '':
            ptitle = cf.meta['page_type']+' '+str(cf.meta['published'])
        else:
            ptitle = cf.meta['title']

    return ptitle

# site routes

@site.route('/images/<subdir>/<name>')
def images(subdir, name):

    """
    Static image file delivery.
    Serves image files from the project folder.
    """

    path = os.path.join(current_app.config['IMAGE_DIR'], subdir)

    return send_from_directory(path, name)


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
                    feed_url=url_for('.atom_feed'),
                    url=current_app.config['DOMAIN'])
    comic_feed = page_feed(pages, current_app.config['FEED_COUNT'])
    for cf in comic_feed:
        feed.add(feed_helper(cf),
                 content_type='html',
                 url=url_for('.comic_page',
                             book=cf.meta['book']['title'],
                             chapter=cf.meta['book']['chapter'],
                             number=cf.meta['book']['page_number'],
                             name=cf.path.replace(current_app.config['BOOK_DIR']+'/', '')),
                 published=cf.meta['published'],
                 updated=cf.meta['modified'],
                 summary=cf.body)
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
    Route for news post pages
    """

    path = '{}/{}'.format(current_app.config['NEWS_DIR'], name)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@site.route('/<book>/c<int:chapter>/p<int:number>/<name>.html')
def comic_page(book, chapter, number, name):

    """
    variables after 'p' are used to create pagination links within book stories.
    These are only passed into the comic.html template and only work on
    'comic_page' urls
    """

    path = '{}/{}'.format(current_app.config['BOOK_DIR'], name)
    p = pages.get_or_404(path)

    current_page = p.meta['book']['page_number']
    current_book = p.meta['book']['title']
    current_chapter = p.meta['book']['chapter']

    first_num = first_last(pages, current_book, 'fnum')
    last_num = first_last(pages, current_book, 'lnum')
    minus = current_page - 1
    plus = current_page + 1

    first_page = (fp for fp in pages if first_num == fp.meta['book']['page_number'] and current_book == fp.meta['book']['title'])
    last_page = (lp for lp in pages if last_num == lp.meta['book']['page_number'] and current_book == lp.meta['book']['title'])
    previous_page = (pp for pp in pages if minus == pp.meta['book']['page_number'] and current_book == pp.meta['book']['title'])
    next_page = (np for np in pages if plus == np.meta['book']['page_number'] and current_book == np.meta['book']['title'])

    return render_template(
        'comic.html',
        current_book=current_book,
        current_chapter=current_chapter,
        p=p,
        previous_page=previous_page,
        next_page=next_page,
        last_page=last_page,
        first_page=first_page
    )

# build function

def chill():

    """
    Function responsible for generating static files
    """

    walk_directory(cfg['IMAGE_DIR'])
    freezer.freeze()
