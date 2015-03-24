# 3color press

(project name changed from temporary comicr)

This is a Flask app to intended generate a static website for comics from markdown files using the flask and various extensions. The name is currently just a placeholder.

Each page is built from a markdown file located in the instance/content/ folder. Right now I have a few examples placed. They have header containing metadata followed by a markdown body, which is currently just a link to the comic page located in the instance/images folder.

I am new to programming and I'm kind of brute learning python and flask by just working on this project.

For more in depth information on how to use check [the how to page](http://3color.noties.org/HowTo.html)

TODO:

  * clean and fix atom feed and look into datetime problem
  * make clean default template and example site
  * look into better usage of YAML header tags and page metadata
  * continue sliming and improving options
  * format code, better error checking


For credit I have been using the following as references as well as documentation.

   * <https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/>
   * <http://royprins.com/add-flatpages-to-flatfreeze>
   * <http://obsoleter.com/2012/12/12/creating-plume-a-static-site-generator-with-flask-part-1/>
   * <https://pythonhosted.org/Flask-FlatPages/>
   * <https://pythonhosted.org/Frozen-Flask/>
