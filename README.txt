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
 * easily add a page to the main menu
 * easily add custom single pages
 * News page to collect news feed page
 * Support for showing a thumbnail of most recent comic in desired story line on every page
 * command line tools for easy management

In Progress Features

 * custom themeing support
 * toggle-able theme elements
 * base site building improvement
 * page editing
 * better error checking
 * admin gui interface
 * import from drupal/sql tool


Installation
-------------

The package is available in pypi::

  $ pip install 3color-Press

For developer minded peoples:
-----------------------------

This packages uses:

* Flask, Flask-FlatPages, Frozen-Flask for site building.
* Fabric for ssh interactions
* Click for the command line tool

Contribute
----------

If you're interested in contributing or checking out the source code you can take a look at:

 * Issue Tracker: https:github.com/chipperdoodles/3color/issues
 * Source Code: https:github.com/chipperdoodles/3color


Support
-------

If you're having problems or have some questions,
feel free to check out the github page: https://github.com/chipperdoodles/3color

Documentation can be found at: https://pythonhosted.org/3color-Press/

The package can be found on pypi at: https://pypi.python.org/pypi/3color-Press/0.2.1

License
--------

3color-Press is (c) Martin Knobel and contributors and is licensed under a BSD license
