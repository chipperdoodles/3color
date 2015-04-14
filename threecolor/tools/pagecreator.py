import os
import yaml

from datetime import date
from ..models import pageHeader

class pagesCreator(pageHeader):

    def __init__(self, **kwargs):

    page_amount = range(1, input+1)
    index = 0
    pub = '{:%Y-%m-%d}'.format(date.today())
    mod = '{:%Y-%m-%d}'.format(date.today())


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

class pageCreator(pageHeader):

    def __init__(self, **kwargs):

        self.__dict__.update(kwargs)
        self.pub = '{:%Y-%m-%d}'.format(date.today())
        self.mod = '{:%Y-%m-%d}'.format(date.today())
