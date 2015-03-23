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

Each page is built from a markdown file located in the content/ folder. Right now I have a few examples placed. They have header containing metadata followed by a markdown body, which is currently just a link to the comic page located in the static/images folder.

I am new to programming and I'm kind of brute learning python and flask by just working on this project.


For more in depth information on how to use check [the how to page](3color.noties.org/HowTo.html)

TODO:

  * clean and fix atom feed and look into datetime problem
  * better jinja2 block usage in templates
  * child menu links?
  * make clean default template and example site
  * look into better usage of YAML header tags and page metadata
  * figure out file naming convention for comic pages


For credit I have been using the following as references as well as documentation.

   * <https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/>
   * <http://royprins.com/add-flatpages-to-flatfreeze>
   * <http://obsoleter.com/2012/12/12/creating-plume-a-static-site-generator-with-flask-part-1/>
   * <https://pythonhosted.org/Flask-FlatPages/>
   * <https://pythonhosted.org/Frozen-Flask/>
