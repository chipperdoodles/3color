Quickstart
==========

This is a quickstart guide for getting up and running fast

If you're an end user not too familiar with python or working in the command line check out:
:doc:`new_users/index`

Installation
------------
see  :doc:`new_users/install` for in depth help

If you have python and pip installed on your computer::

  $ pip install 3color-Press

this will install to your site packages folder and create the 3color-Press project
folders in your home directory, and will also make the 3color command line tool
available in your path. (current exceptions if you install with --user flag, the
3color tool will be in in userbase/bin )

If you have problems with system permissions (i.e. you use osx's native python)
Look into using virtualenv or installing with --user and adding appropriate path
for the command line tool into your system path.


Usage
-------
see :doc:`Users/commands` for more about the 3color tool

The command line tool 3color allows for some quick access for
managing, building, pushing, testing your site, as well as bootstrapping new page creation.

``3color run``

This command will run the site live and locally on port 5000 as well as open your
default browser to it. (if it doesn't load just refresh and currently the browser)

Configure
---------
see :doc:`Users/setup` for more info

Edit the settings.cfg file in your :term:`project folder`

Make pages
----------
see :doc:`Users/pages` for more info

Simply write
