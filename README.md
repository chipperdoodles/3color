# comicr

This is a Flask app to intended generate a static webcomic site from markdown files using flatpages. I realize the name is dumb, I just needed something to make a directory while I started on it.

to generate static files type `python generator.py build` and to run with flask's built in webserver in debug just type `python generator.py`

Each page is built from a markdown file located in the pages/ folder. Right now I have a few examples placed. They have a ymal header followed by a markdown body, which is currently just a link to the comic page located in the static/images folder.

I am new to programming and I'm kind of brute learning python and flask by just working on this project. for credit I have been using https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/ for help as well as documentation for flask and the various extentions.

relies on:
 * Flask
 * Flask-Flatpages
 * Flask-Freeze


    pip freeze >
    Flask==0.10.1
    Flask-FlatPages==0.6
    Frozen-Flask==0.11
    itsdangerous==0.24
    Jinja2==2.7.3
    Markdown==2.5.2
    MarkupSafe==0.23
    PyYAML==3.11
    Werkzeug==0.10.1
    WTForms==2.0.2
