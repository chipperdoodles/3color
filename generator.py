import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('home.html', pages=pages)

@app.route('/books/')
def books():
    firstpage = (p for p in pages if p.meta['chapter'] == 1 and p.meta['number'] == 1)
    return render_template('books.html', pages=firstpage)

@app.route('/books/<string:book>/')
def chapters(book):
    chapters = (p for p in pages if p.meta['book'] == book and p.meta['number'] == 1)
    return render_template('books.html', pages=chapters)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
