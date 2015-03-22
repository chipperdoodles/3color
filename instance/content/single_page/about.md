title: "About"
published: 2015-02-17
page_type: single_page
book:
chapter:
page_number:
image:
menu: True

This is a sample static page written in the markdown language, then generated into html with the help of Flask, Flask-Flatpages, and Frozen-Flask. The goal of this project is to have a static site generator with a template that covers the basic needs of a webcomic website. I currently use drupal for my webcomic, but felt like it has been too much for my needs. In addition to that I have always felt I needed to hack too much of it for a default webcomic layout. Although I love my site, I decided to give building a static-site generator a try. the Flask-Flatpages and Frozen-Flask extensions for Flask gave me an easy way to start that.

It's kind of a mess right now, but I'm learning. if you're interested head over to the [github page](https://github.com/chipperdoodles/3color) and check out the source code.
The static site generator part of this project is just part 1 of a bigger idea, but is a good starting place and will be completely functional on it's own

Sample comics taken from my personal webcomic site <a href="https://noties.org">noties.org</a>

features so far:

 * automatic book pagination (first, back, next, latest) based on which book it belongs to.
 * different page(or post) types. Books(for comic storylines or just one comic), News(for news updates), Single_Page(for site pages like about, contact, readme)
 * can automatically display the most recent comic on the front page
 * a /books/ page that will automatically list the books and their respective pages
 * a /news/ page that acts as a feed of news posts. This can also be displayed on the front page
 * the html templates use jinja2 so skinning and theming should be pretty accessible.
 * builds your entire site into static html files which can be easily hosted from any web hosting service
 * current template includes keyboard navigation for previous and next pages
 * a main menu option if yes then a link for the page will appear in the main menu
 * if using osX or linux, the ability to publish files with sftp and rsync
