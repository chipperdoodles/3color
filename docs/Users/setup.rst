Project set up
==============

Project folder
---------------

The :term:`project folder` is a folder in user's home directory named 3color-Press.
This should be created upon install along with copying over an example settings file
and the neccesary subfolders.

This is your folder! It holds all of the custom data and files you add and create
that will be turned into your website.

On fresh install it should look like this: ::

        3color-Press/
      ├── content
      │   ├── book
      │   ├── news
      │   ├── gallery
      │   └── single
      ├── example.settings.cfg
      ├── images
      │    ├── comics
      │    ├── gallery
      │    └── misc
      ├── settings.cfg
      └── themes

if you do not have a :file:`example.settings.cfg` and :file:`settings.cfg` run the
command ``3color setup``


Post Install Set up
--------------------

You can double check to see if :term:`project folder` exists after installing by
browsing to your home folder and looking for the folder 3color-Press.

.. note::
    (Unix) if you installed using sudo, you probably do not have write permissions
    to this folder and it's contents and will need to fix that.

If you see the files in there, great! Your first step should be editing the
settings.cfg to configure your site.

Configuration
-------------

For the site, 3color provides an example settings file which can be saved as
settings.cfg. The example file explains the configuration options and should be
relatively straightforward.
