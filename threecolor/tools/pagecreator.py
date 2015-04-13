import os
import yaml

from datetime import date
from ..models import page_header

def pages_creator():

    shortname = str(raw_input("Shortbook name, one word: "))
    longname = raw_input("Long name for book, the book's title: ")
    pagetype = raw_input("Page type of pages to be made. These are book, news, or single: ")
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

    return write_page()

class page_creator(page_header):

    def __init__(self, **kwargs):

        pub = '{:%Y-%m-%d}'.format(date.today())
        mod = '{:%Y-%m-%d}'.format(date.today())

    def write_page(self):
            name = self.shortname+'_'+str(self.pagenumber)+'.md'
            with open(name,"ab") as f:
                yaml.dump(self.header(), f)

    def print_page(self):

            name = self.shortname+'_'+str(self.pagenumber)+'.md'
            stuff = yaml.dump(self.header)
            return stuff
