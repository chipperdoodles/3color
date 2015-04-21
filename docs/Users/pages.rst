Page Management
===============

Page files are text files located in your 3color-Press/content/<pagetype> folder.
If you notice there are three different folders in the content folder. These are
book, news, and single. The files for their respective :term:`page type` go in apropriate folders.


The text files are have a special header on the top that provides the needed
information to properly organize and create your page

The Page Header
^^^^^^^^^^^^^^^
The :term:`page header` will look something like this: ::

  title:
  published: yyyy-mm-dd
  modified: yyyy-mm-dd
  page_type:
  book: { 'title': , 'chapter': , 'page_number': , 'image': }
  menu:
  version: 0.2.1

.. note::
    if using the autogenerate tool all items will be alphabetically sorted and not in the
    same order as above, however all the information will be there and the same.
    As long as each field is correctly typed and filled in, it doesn't matter what order
    key: value is in. (for programmers: b/c dict)

* title is the title of the page, it shows up on the webpage for the default template.
* published is the date you post it in yyyy-mm-dd
* modified is the date if you want to post changes to the file. Not currently used, in here as a just in case
* page_type is the type of this page. Available choices are: book, news, single.
* book: is where you fill out info for your book pages. Title is book title, chapter is chapter number, page_number is the page number
  and image is the name of your comic image file uploaded in your images folder.
  (chapter and page_number are integers and image has to include your filename extension such as .png or .jpg)
* menu is a True or False statement. If marked true and entry for this page will be automatically added to the main menu
* version is the version of 3color-Press the page was created with

Example headers:

for page type book: ::

    title: Ricks Page 3
    published: 2016-02-18
    modified: 2016-02-18
    page_type: book
    book: { 'title': Ensign Ricks, 'chapter': 2, 'page_number': 3, 'image': rick_15.png }
    menu: False
    version: 0.1


for page type single: ::

    title: Contact
    published: 2016-03-01
    page_type: single
    book: { 'title': "", 'chapter': '', 'page_number': '', 'image': "" }
    menu: True
    version: 0.1

    If you need to reach me you can find me on the [tweeters](https://twitter.com/chipperdoodles)

.. note::
   notice how files for page type book differ slightly from files for news and single pages.
   This is only because as is now, the html template for book pages automatically
   displays the comic image for you. In single and news there is actually written
   content added. Everything after the last header tag (with a blank line inbetween)
   Is read as the body and can be written in markdown syntax (easy to remember)
   or even html.

.. note::
   Since we're in early dev be wary that the information in page header may grow
   and change as will the default template designs that use such information.


The Page Body
^^^^^^^^^^^^^
  .. todo::
      explain markdown syntax and the page body

Creating a new page file
---------------------------

You can do this many ways. 3color has a command that bootstraps the creation of a new page.
This is the ``3color newpage`` command. When run it will ask the user for inputs, these in
turn will be used to create a new file with a premade header filled by your input.

This helps avoid arduously re-writing the header line everytime you make a new page file.

If you just made a file of the page type 'book', the only step you'd have to do is
to make sure to copy over your comic image file to your images folder. (:file:`3color-Press/images`)

If you just made a file of the types news or single then you have to now add the :term:`page body` .
If using atom as your editor you can run ``3color atom`` to open up your project folder with atom.
Just browse to content/pagetype directory of the file you made in the atom tree/file browser
(the thing on the left hand side of the atom editor) find your file, select it and start
writing in the body content of your page, save, and then you have your new page.

You can obviously use your own text editor to create page files manually, just
be sure to save in the appropriate page type content folder as well as fill out
the header correctly.

Now to test our site and see our new pages we can look use ``3color run`` from
:doc:`commands` to see a live example of our website.

.. note::
   3color-Press doesn't currently have a set default theme, to get the best results
   you can copy the :file:`threecolor/site/templates` and :file:`threecolor/site/static folders`
   to :file:`themes/NEWTHEME/templates` :file:`themes/NEWTHEME/templates`. If you know
   a bit of css and html you should be able to figure out how to make a theme no problem.
   suggested reading if you want to do more would be the jinja2 documentation.
