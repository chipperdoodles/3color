import os
import sys
import yaml

from . import __version__
from datetime import date
from application import page_dir

class pageHeader(object):

    def __init__(self, **kwargs):

        # self.longname = kwargs['longname']
        # self.pagetype = kwargs['pagetype']
        # self.pageamount = kwargs['pageamount']
        # self.pagetitle = kwargs['pagetitle']
        # self.pagenumber = kwargs['pagenumber']
        # self.published = kwargs['pub']
        # self.modified = kwargs['mod']
        # self.image = kwargs['image']
        # self.menu = kwargs['menu']
        self.__dict__.update(kwargs)

    @property
    def header(self):

        header = dict(
            title = self.pagetitle,
            published = self.pub,
            modified = self.mod,
            page_type = self.pagetype,
            book = {'title': self.longname, 'chapter': self.chapter,
                    'page_number': self.pagenumber, 'image': self.image},
            menu = self.menu,
            version = __version__ )

        return header

    def write_page(self, path):
            name = os.path.join(path, self.shortname+'_'+str(self.pagenumber)+'.md')
            with open(name,"ab") as f:
                yaml.dump(self.header, f)

    def dump(self):
        name = os.path.join(self.path, self.shortname+'_'+str(self.pagenumber)+'.md')
        info = yaml.dump(self.header)
        return name+'\n'+info

class pagesCreator(pageHeader):

    def __init__(self, **kwargs):

        self.__dict__.update(kwargs)
        self.index = 0
        self.pub = '{:%Y-%m-%d}'.format(date.today())
        self.mod = '{:%Y-%m-%d}'.format(date.today())

    def header(self, n):

        header = dict(
            title = '',
            published = self.pub,
            modified = self.mod,
            page_type = self.pagetype,
            book = {'title': self.longname, 'chapter': '', 'page_number': n, 'image': ''},
            menu = False,
            version = __version__ )

        return header

    def write_page(self):

        for x in range(1, self.page_amount+1):
            name = os.path.join(self.path, self.shortname+'_'+str(self.index+x)+'.md')
            number = self.index+x
            with open(name,"ab") as f:
                yaml.dump(self.header(number), f)

class pageCreator(pageHeader):

    def __init__(self, **kwargs):

        self.__dict__.update(kwargs)
        self.pub = '{:%Y-%m-%d}'.format(date.today())
        self.mod = '{:%Y-%m-%d}'.format(date.today())
