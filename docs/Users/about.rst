About 3color-Press
==================

Why blogs? What about comics!?!


What the heck is it?
-------------------

Simple version: easily build and maintain your comic site on your computer, then
just as easily upload the changes to your host webserver.


A little more detail and background
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3color-Press is an attempt to bridge a dynamic cms (wordpress, drupal, etc) and
a static site generator (Jekyll, Pelican-Blog). However it is entirely focused on comics.

As a huge nerd and a webcomic artist, I have been responsible for creating,maintaining,
designing, and hosting my website (It took quite a few years to get there).
I noticed that most cms and similar website management/creation tools and programs out there
were primarily focused on blog first, or enterprise website, or store front. However there
weren't any similar ones that focused on my favorite kind of website, a comic site. With
some weird determination and hopeful eyes I set on trying to make something that fit that
gap. I've tried to include base needs of a standard web comic site into the design, but many
features are to be added. Feedback is appreciated!


Ok cool, but what does any of that mean?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To make it simple you can think of 3color-Press as a website building program/application.
It is meant to make it easy to add new pages, update, and maintain a comic website.

Wordpress, Drupal and other blogging and cms tools usually are programs/apps that run
on a server which you access through the internet. 3color-Press runs on your computer
and only communicates with your webserver when you chose to publish changes.

A static-site generator takes input, runs it and then creates a folder of html/css/static
files, which can then be uploaded and hosted on any websever. It makes it a lot
easier than painfully rewriting code, but also a lot safer than running a dynamic site tool like wordpress.
Static sites also have the added benefit of performance with a flexibility of hosting.

As it is right now 3color-Press is single user minded, meaning that it does not
have user accounts, or comments. (though comments could be added via a service like disqus).


Basic how it works
------------------

3color-Press uses text files instead of a database for page creation and saving settings.
The Text files are, by default, markdown files with a YAML header in the top of the file.
The YAML header provides all the page metadata while everything else written in markdown
gets generated into html.


3color-Press creates the :term:`project folder` on install and this is where you
will have all your custom website info. (pages, themes, images).
