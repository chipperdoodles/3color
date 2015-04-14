import os
import yaml

from datetime import date
from ..models import pageHeader
from .. import __version__

class pagesCreator(pageHeader):

    def __init__(self, **kwargs):

        self.__dict__.update(kwargs)
        self.page_amount = range(1, page_amount+1)
        index = 0
        pub = '{:%Y-%m-%d}'.format(date.today())
        mod = '{:%Y-%m-%d}'.format(date.today())

    @property
    def header(self, numb):

        header = dict(
            title = None,
            published = pub,
            modified = mod,
            page_type = pagetype,
            book = {'title': longname, 'chapter': None, 'page_number': numb, 'image': None},
            menu = False,
            version = __version__ )

        return header

    def write_page(self):
        for x in self.page_amount:
            name = os.path.join(self.path, self.shortname+'_'+str(index+x)+'.md')
            number = index+x
            with open(name,"ab") as f:
                yaml.dump(self.header(number), f)

        return write_page()

class pageCreator(pageHeader):

    def __init__(self, **kwargs):

        self.__dict__.update(kwargs)
        self.pub = '{:%Y-%m-%d}'.format(date.today())
        self.mod = '{:%Y-%m-%d}'.format(date.today())
