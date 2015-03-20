title: "ReadMe"
published: 2015-02-26
page_type: single_page
book:
chapter:
page_number:
image:
menu: True

# 3color press

This is a Flask app to intended generate a static webcomic site from markdown files using the flask extension flatpages. The name is currently just a placeholder.

To generate static files type `python press.py build`

To run live with flask's built in web-server in debug just type `python press.py` and visit localhost:5000 in your browser

Each page is built from a markdown file located in the content/ folder. Right now I have a few examples placed. They have header containing metadata followed by a markdown body, which is currently just a link to the comic page located in the static/images folder.

I am new to programming and I'm kind of brute learning python and flask by just working on this project.

For credit I have been using the following as references as well as documentation.

 * <https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/>
 * <http://royprins.com/add-flatpages-to-flatfreeze>
 * <http://obsoleter.com/2012/12/12/creating-plume-a-static-site-generator-with-flask-part-1/>
 * <https://pythonhosted.org/Flask-FlatPages/>
 * <https://pythonhosted.org/Frozen-Flask/>

requirements:

 * Flask
 * Flask-Flatpages
 * Flask-Freeze

suggested:

 * python virtualenv

TODO:

  * clean and fix atom feed and look into datetime problem
  * better jinja2 block usage in templates
  * push build with ftp/sftp/rsync (not to hard add)
  * child menu links?
  * make clean default template and example site
  * look into better usage of YAML header tags and page metadata
  * figure out file naming convention for comic pages

## Directory Structure
here is the layout of the project

---

        3color/
        ├── MANIFEST.in ///file for setup tools
        ├── README.md
        ├── instance /// this folder contains files you create to be made into web pages and images for your comics
        │   ├── content
        │   │   ├── comics
        │   │   │   └── ///Book page markdown files go here 'bookpagename.md'
        │   │   ├── news
        │   │   │   └── ///News page markdown files go here 'newspagename.md'
        │   │   └── single_page
        │   │       └── ///Single page markdown files go here 'singlepagename.md'
        │   ├── images
        │   │   └── /// all images for the comics go here turbodeck2.png
        │   └── settings.cfg ///this is a configuration file a user can edito for site info
        ├── press.py /// main python file to run from the terminal
        ├── push-pages.sh // this is a shell script to push my built output to my gh-pages branch with git
        ├── requirements.txt /// a pip freeze
        ├── setup.py /// distutils script
        └── threecolor /// the package that handles building your comic site
            ├── __init__.py
            ├── default_settings.py ///Settings file that sets the defaults for your site, is overridden by settings.cfg in your instance folder
            ├── flatpager.py
            ├── static ///static files, holds all static files for the template design these define the look of your site
            │   ├── css
            │   │   ├── fonts.css
            │   │   ├── main.css
            │   │   └── mainprefixed.css
            │   ├── fonts
            │   │   └── sourceSans
            │   │       └── SourceSansPro.ttf
            │   └── images
            │       └── retina_wood.png
            └── templates /// jinja2 templates, these define the layout of your site
                ├── _book_nav.html
                ├── _latest.html
                ├── _menu.html
                ├── archive.html
                ├── base.html
                ├── books.html
                ├── chapters.html
                ├── comic.html
                ├── home.html
                ├── news.html
                ├── page.html
                └── test.html


---
## file structure for text files in content folders
Pages are markdown files with a pyaml header followed by an empty line and then the post content. They are put in the folder the corresponds for their type. The types `news` and `single_pages` have a blank field for `book: chapter: page_number: image:`. For the type of book, you don't need to write anything after main-menu, just make sure that`image: ""` has the correct filename for your comic page image.

for comic pages:

    :::yaml
    title: "Ricks Page 3"
    published: 2016-02-18
    page_type: book
    book: "Ensign Ricks"
    chapter: 2
    page_number: 3
    image: "rick_15.png"
    menu: False


for news and single_page :

    :::yaml
    title: "Contact"
    published: 2016-03-01
    page_type: single_page
    book:
    chapter:
    page_number:
    image:
    menu: True

    If you need to reach me you can find me on the [tweeters]("https://twitter.com/chipperdoodles")
