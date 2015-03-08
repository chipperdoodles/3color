# 3color Press

(project name changed from temporary comicr)

This is a Flask app to intended generate a static webcomic site from markdown files using the flask extension flatpages. The name is currently just a placeholder.

To generate static files type `python generator.py build`

To run live with flask's built in web-server in debug just type `python generator.py` and visit localhost:5000 in your browser

Each page is built from a markdown file located in the content/ folder. Right now I have a few examples placed. They have header containing metadata followed by a markdown body, which is currently just a link to the comic page located in the static/images folder.

An example of a site built with comicr is hosted on github pages and can be found at http://comicr.noties.org

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

TODO
 * clean and fix atom feed and look into date-time problem
 * better {% block %} usage in templates
 * push build with ftp/sftp/rsync(not to hard add, will put in once I settle on templates and file format)
 * child menu links?
 * make clean default template and example site
 * look into better usage of YAML header tags and page metadata
 * figure out file naming convention for comic pages

### Directory Structure
here is the layout of the project
---
```
comicr
├── README.md
├── content
│   ├── books
│   │   └── ///Book page markdown files go here 'bookpagename.md'
│   ├── news
│   │   └── ///News page markdown files go here 'newspagename.md'
│   └── single_page
│       └── ///Single page markdown files go here 'singlepagename.md'
├── flatpager.py /// the app module for now
├── default_settings.py /// contains default and app settings
├── images
│   └── /// all images for the comics go here turbodeck2.png
├── push-pages.sh /// this is a shell script to the build folder gh-pages to my gh-pages branch
├── requirements.txt /// a pip freeze
├── settings.cfg /// currently not in use
├── static ///static files flask convention, holds all static files for the template design these define the look
│   ├── css
│   │   └── main.css
│   ├── fonts
│   │   └── sourceSans
│   └── images
│       ├── lined_paper.png
│       ├── logo.png
│       └── retina_wood.png
└── templates /// jinja2 templates, these define the layout
    ├── _book_nav.html
    ├── _latest.html
    ├── _menu.html
    ├── base.html
    ├── books.html
    ├── comic.html
    ├── home.html
    ├── news.html
    └── page.html
```

---
## file structure for text files in content folders
Pages are markdown files with a pyaml header followed by an empty line and then the post content. They are put in the folder the corresponds for their type. The types `news` and `single_pages` have a blank field for `book: chapter: page_number: image:` . For the Type of book, the post is simply a jinja formatted link with the `name` = the filename located in the images folder.

for comic pages:
```yaml
title: "Ricks Page 3"
published: 2016-02-18
page_type: book
book: "Ensign Ricks"
chapter: 2
page_number: 3
image: "rick_15.png"
menu: False

```

for news and single_page :
```yaml
title: "Contact"
published: 2016-03-01
page_type: single_page
book:
chapter:
page_number:
image:
menu: True

If you need to reach me you can find me on the [tweeters]("https://twitter.com/chipperdoodles")
```
