# comicr

This is a Flask app to intended generate a static webcomic site from markdown files using flatpages. The name is currently just a placeholder.

To generate static files type `python generator.py build` and to run with flask's built in webserver in debug just type `python generator.py`

Each page is built from a markdown file located in the content/ folder. Right now I have a few examples placed. They have header containing metadata followed by a markdown body, which is currently just a link to the comic page located in the static/images folder.

I am new to programming and I'm kind of brute learning python and flask by just working on this project.

For credit I have been using the following as references as well as documentation.
 * https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/
 * http://royprins.com/add-flatpages-to-flatfreeze
 * http://obsoleter.com/2012/12/12/creating-plume-a-static-site-generator-with-flask-part-1/
 * https://pythonhosted.org/Flask-FlatPages/
 * https://pythonhosted.org/Frozen-Flask/

Relies on:
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
