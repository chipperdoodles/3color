title: ReadMe
published: 2015-02-26
book: none
chapter:
page_number:
main-menu: yes

# comicr

This is a Flask app to intended generate a static webcomic site from markdown files using the flask extension flatpages. The name is currently just a placeholder.

To generate static files type `python generator.py build`

To run live with flask's built in web-server in debug just type `python generator.py` and visit localhost:5000 in your browser

Each page is built from a markdown file located in the content/ folder. Right now I have a few examples placed. They have header containing metadata followed by a markdown body, which is currently just a link to the comic page located in the static/images folder.

I am new to programming and I'm kind of brute learning python and flask by just working on this project.

For credit I have been using the following as references as well as documentation.

 * https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/
 * http://royprins.com/add-flatpages-to-flatfreeze
 * http://obsoleter.com/2012/12/12/creating-plume-a-static-site-generator-with-flask-part-1/
 * https://pythonhosted.org/Flask-FlatPages/
 * https://pythonhosted.org/Frozen-Flask/

requirements:

 * Flask
 * Flask-Flatpages
 * Flask-Freeze

suggested:

 * python virtualenv
