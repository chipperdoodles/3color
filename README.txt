About
======

3color Press is a flask based application intended to streamline making your own comic based website.
It is a static website generator that takes markdown formatted text files and turns them into new pages.

I am new to programming and I'm kind of brute learning python and flask with this project.
The project is under heavy development and features are being added as we work on them,
however a very functional core set of features is included

For more in depth information on how to use check the doc pages You can see a demo
site generated with version 0.1 of this tool at http://3color.noties.org

Features

 * automatic handling of book pages, news pages and single pages
 * automatic pagination for book pages
 * easily add custom single pages
 * News page to collect news feed page
 * Support for showing a thumbnail of most recent comic in desired story line on every page
 * command line tools for easy management
 * custom themes
 * gallery page and items

In Progress Features
 * cleaning up and ironing out
 * base site building improvement
 * better error checking
 * admin gui interface
 * import from drupal/sql tool


For Webcomic artists and end users that are interested:
_______________________________________________________

This is intended as a tool to replace using something like comicpress/wordpress.
I have my own comic so this is taken from my needs in site design. It's under heavy
development and I would love feedback. However in it's early form the to use 3color,
some knowledge of python dev environments and basic command line will be necessary.
I highly encourage those who are curious enough to learn a bit to get around. If
you have used a word press or drupal you might be able to see similarities in the
folder organization for themes and config files and such.

If you are curious feel free to contact me mknobel@noties.org

Installation
-------------
NOTE: the pypi package is out of date

to test the latest:

   (I suggest the use python virtualenv)
   clone the master branch with git or download the zip from github

   $ pip install -e /path/to/gitclone/directory

out of date package instructions:

The package is available in pypi::

  $ pip install 3color-Press

For developer minded peoples:
-----------------------------

This packages uses:

* Flask, Flask-FlatPages, Frozen-Flask for site building.
* Fabric for ssh interactions
* Click for the command line tool
* there might be some stragglers I forgot to add in dependency

Contribute
----------

If you're interested in contributing or checking out the source code you can take a look at:

 * Issue Tracker: https:github.com/chipperdoodles/3color/issues
 * Source Code: https:github.com/chipperdoodles/3color


Support
-------

NOTE: Documentation is out of date, some of it might still be applicable but the
a lot of things have changed. The data of each .md page files specifically have
changed and I would suggest using the newpage command to create a new blank page
to view as a template. I plan on updating the documentation once the command line
version of 3color has a stable launch and is up on pypi.

If you're having problems or have some questions,
feel free to check out the github page: https://github.com/chipperdoodles/3color

Documentation can be found at: https://pythonhosted.org/3color-Press/

The package can be found on pypi at: https://pypi.python.org/pypi/3color-Press/0.2.1

author_email: mknobel@noties.org

License
--------

3color-Press is (c) Martin Knobel and contributors and is licensed under a BSD license
