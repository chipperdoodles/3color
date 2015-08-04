Theming Variables
=================

There's a list of variables available for themers


Global Variables
----------------
pages - generated object which holds all the .md files turned pages of your website

main_menu - pages in which main_menu is in the menuname list

book_pages - pages of the book page_type

news_pages - pages of the news page_type

gallery_items - items with the gallery page_type

thumb_nail - page to display as thumbnail


home ("/") page variables
-------------------------
front_page - most recent MAIN_STORY page to display on front page


comic page variables
--------------------
current_book - pages whose book title matches the book of the current page
current_chapter - pages whose chapter number matches the current chapter
p - the page
previous_page - the page whose page_number = current page -1
next_page - the page whose page_number is +1 of the current page
t_pages - total pages in the book
last_page - page_number that is the total pages
first_page - first page in the book (page 1)

books page variables
--------------------
first_page - books that are page 1 and unique in name
