Theming for 3color Press
========================

3color Press is being designed with theming in mind, that being said it's still
a work in progess. It uses flask/jinja two templating language and is pretty easy
to get into.

The current version of 3color Press allows you to override the default theme by
providing your own theme in the project folder/themes folder and setting your configuration
to use it.

You can use the default theme as a base with the ``3color newtheme`` command.
this will create a new theme of your name choice in your themes folder. It also
copies over the theme_settings.cfg file which can be used to change basic things
such as background colors.
(new as of 0.2.2)


Theme folder layout
-------------------
The theme folder is simply a flask styled folder which must include the following two folders:

*static* - This is where css, images, and javascript folders and files go

example ::

    -static
        -css // any and all css files
          main.css
        -js // any js scripts or libraries
          script.js
        -images // static images for site backgrounds and logos
          logo.png


*templates* - this is where you make your jinja html templates.
  This must contain the following files as for now these pages are rendered:

  -templates

      * home.html
      * page.html
      * books.html
      * comic.html
      * news.html
      * gallery.html


Theming todo
-------------

In the development list on two do is providing more configurable variables for
templates. (such as toggling pages or elements like the logo header and site name)
as well as provide a theme bootstrap command to create new themes and provide an
example default theme.
