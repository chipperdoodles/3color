import sys
import os
import yaml

from datetime import date

# def pages_creator():

shortname = str(raw_input("shortbook name, one word: "))
longname = raw_input("long name for book, the book's title: ")
pagetype = raw_input("page type of pages to be made. These are book, news, or single_page: ")
page_amount = range(1, input("amount of pages to create (in digits): ")+1)
index = 0

def page_header(numb):

    pub = '{:%Y-%m-%d}'.format(date.today())
    mod = '{:%Y-%m-%d}'.format(date.today())

    header = dict(
        title = '',
        published = pub,
        modified = mod,
        page_type = pagetype,
        book = {'title': longname, 'chapter': '', 'page_number': numb, 'image': ''},
        menu = False,
        version = 0.1 )

    return header

def write_page():
    for x in page_amount:
        name = shortname+'_'+str(index+x)+'.md'
        number = index+x
        with open(name,"ab") as f:
            yaml.dump(page_header(number), f)

write_page()
