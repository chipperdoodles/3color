# comicr

This is a Flask app to intended generate a static webcomic site from markdown files using flatpages. I realize the name is dumb, I just needed something to make a directory while I started on it.

to generate static files type `python generator.py build` and to run with flask's built in webserver in debug just type `python generator.py`

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
