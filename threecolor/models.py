import os
import yaml

from . import __version__
from datetime import date


class PageHeader(object):
    """
    Class that handles page header data. The page header is a yaml header
    at the beginnning of the markdown file that will be turned into an page.
    """

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
        """
        Make a dict from kwargs
        """
        return {
            "title": self.pagetitle,
            "published": self.pub,
            "modified": self.mod,
            "page_type": self.pagetype,
            "book": {
                'title': self.longname,
                'chapter': self.chapter,
                'page_number': self.pagenumber,
                'image': self.image
            },
            "menu": self.menu,
            "version": __version__
        }

    def write_page(self):
        """ Writes the dict from header funtion into a file. This is our page metadata information"""
        name = os.path.join(self.path, self.shortname+'_'+str(self.pagenumber)+'.md')
        with open(name, "ab") as f:
            yaml.dump(self.header, f)

    def dump(self):
        """test function"""
        name = os.path.join(self.path, self.shortname+'_'+str(self.pagenumber)+'.md')
        info = yaml.safe_dump(self.header)
        return name+'\n'+info


class PagesCreator(PageHeader):

    """Subclass of PageHeader for making batch yaml headers and markdown files"""

    def __init__(self, **kwargs):
        super(PagesCreator, self).__init__(**kwargs)
        self.index = 0
        self.pub = '{:%Y-%m-%d}'.format(date.today())
        self.mod = '{:%Y-%m-%d}'.format(date.today())

    def header(self, n):

        return {
            "title": '',
            "published": self.pub,
            "modified": self.mod,
            "page_type": self.pagetype,
            "book": {'title': self.longname, 'chapter': '', 'page_number': n, 'image': ''},
            "menu": False,
            "version": __version__
        }

    def write_page(self):
        """ Writes the dict from header funtion into a file. This is our page metadata information"""

        for x in range(1, self.page_amount+1):
            name = os.path.join(self.path, self.shortname+'_'+str(self.index+x)+'.md')
            number = self.index+x
            with open(name, "ab") as f:
                yaml.safe_dump(self.header(number), f)


class PageCreator(PageHeader):

    def __init__(self, **kwargs):
        super(PageCreator, self).__init__(**kwargs)
        self.pub = '{:%Y-%m-%d}'.format(date.today())
        self.mod = '{:%Y-%m-%d}'.format(date.today())
