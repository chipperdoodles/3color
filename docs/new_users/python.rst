Things to know, Python
===========================
  Python (https://www.python.org/) is a well known and well used programming lanuague.
Oh no!, you might say, A programming language? Am I going to have to learn to code?
Nope! Not unless you want to, or if you want furthur customize the guts of the project.

  I'm bringing this up only because it will help to know a bit about having python
on your computer. Since this project depends on python you will need to install it
or check to see if it's installed already on your computer. (it will also help
to know where python stores the related files)


Versions
--------

  Python comes in two main versions, 2.7 and 3.4 (2.7.9 and 3.4.3 respectivly at the time of writing).
The need to know is that this project, although most of it works with python 3,
it currently requires python 2.7 (early versions may work however have not been tested)
due to the packages 3color-Press uses to push a website to remote servers with the
sftp, and rsync protocols(and any transfer that connects to a remote server via ssh).

  As time goes there will be more testing for python3 compatability but for now
python 2.7 is the go to.

  If you want to learn more about choosing python 2 vs python 3 outside of this
project you can visit: https://wiki.python.org/moin/Python2orPython3 .

.. note::

   In shorter words, you need python 2.7.


Installing
----------

  Python is nice and cross platform. This means that 3color-Press should run all the
same one windows, osX, and other operating systems all the same.

  If you are having trouble or are using an older operating system
feel free to visit python's beginner's guide:
https://wiki.python.org/moin/BeginnersGuide/Download


Windows
^^^^^^^

  Python provides official windows installers which can be found at:
  https://www.python.org/downloads/windows/

* download the most recent python 2 release
* run the installer
* if you have admin access you can do all users, if you don't you can just install for your self
* if you want, you can add the python path to the sys path, so you can call python from your terminal you must do it here


OsX
^^^^^

  Macintosh OsX has a default install of python included, however it is not updated.
The latest version of python included in osX Yosemite (10.10) is 2.7.6, which should
be able to run this project. However there are ways of installing and keeping python
up to date on your computer as options. The easiest of ways which is through the
package manager Homebrew (todo: will add homebrew information).


Linux and Unix
^^^^^^^^^^^^^^

  If you're running GNU Linux or a Unix based operating system then right on! You
Probably know enough to not need to be reading this. Just in case you don't, Python
is included in most of these systems and if not are in their package repositories,
and can be installed from as you install other programs.


Pip and PyPi
------------

  Pip is a package management tool for python, It is needed to easily search for, install,
remove, and upgrade python packages. (3color-Press is a python package). If on you installed
the latest python 2 release on windows, pip is already installed for you. (yay!).

  In order to install pip on osX (if you are using osX's included python) it's as simple as
typing ``sudo easy_install pip``

  PyPi (https://pypi.python.org/pypi) is a package repository for python packages.
This is where the 3color-Press package is hosted, along with a lot of other python
packages! There are some very handy tools and fun things uploaded in there which makes
pip a very handy tool!


A Quick Pip intro
^^^^^^^^^^^^^^^^^

let's briefly introduce you to using pip

You can search for packages in pypi with the command: ::

  $ pip search Press

This will pull up packages by name that include the word press, you might see this project in there!

To install a package: ::

  $ pip install packagename

To upgrade a package: ::

  $ pip install --upgrade packagename

To check which packages you have installed: ::

  $ pip list

To check which packages are outdated: ::

  $ pip list --outdated





And there! You should now have enough info to set things up to install 3color-Press
