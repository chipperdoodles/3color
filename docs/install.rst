Installation
============

A more indepth look at installation

for a quickstart go to :doc:`quickstart`


Make sure you have python and pip installed and ready to go.

.. warning::

   Before you run the install command there's a few options and things you need to
   be aware of see Installation options


Installation options
--------------------

running ``$ pip install 3color-Press`` will install the package to your global :term:`site-packages`.
On windows this isn't too much of a worry (testing still needed though) as you shouldn't
get permission denied errors.

on OsX you won't have permission by default to add files to your global :term:`site-packages`,
You will either have to

1. install with root privileges with ``$ sudo pip install 3color-Press``,
2. install user only. ``$ pip install --user 3color-Press``.
3. use a virtualenv

.. note::
  1. (osx/unix) if you install as root it will create your project folder as root
      you can fix this by using ``sudo chown -R username ~/3color-Press`` after you install

  2. If you do option 2 the 3color command won't be available on default. To fix this you can
     run sudo ln -s ~/Library/Python/2.7/site-packages/bin/3color /usr/bin/3color

  3. .. todo: information on virtualenv
