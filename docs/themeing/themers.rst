Theming for 3color Press
========================

3color Press is being designed with theming in mind, that being said it's still
a work in progess. It uses flask/jinja two templating language and is pretty easy
to get into. This Doc is a placeholder for much more info to come.


The current version of 3color Press allows you to override the default theme by
providing your own theme in the project folder/themes folder and setting your configuration
to use it.


Theme folder layout
-------------------
The theme folder is simply a flask styled folder which must include the following two folders:

*static* - This is where css, images, and javascript folders and files go

example ::

    -static
        -css
          main.css
        -js
          script.js
        -images
          logo.png


*templates* - this is where you make your jinja html templates.
  This must contain the following files as for now these pages are rendered:
  * home.html
  * page.html
  * books.html
  * comic.html
  * news.html


Theming todo
-------------

In the development list on two do is providing more configurable variables for
templates. (such as toggling pages or elements like the logo header and site name)
as well as provide a theme bootstrap command to create new themes and provide an
example default theme.
