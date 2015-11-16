import os
import yaml

from . import __version__
from datetime import datetime


class PageHeader(object):

    """
    Class that handles page header data. The page header is a yaml header
    at the beginnning of the markdown file that will be turned into a page.
    """

    def __init__(self, **kwargs):
        self.altt = ''

        self.__dict__.update(kwargs)

        if self.pagenumber is not None:
            self.name = os.path.join(self.path, self.shortname+'_'+str(self.pagenumber)+'.md')
        else:
            self.name = os.path.join(self.path, self.shortname+'_'+str(datetime.now().isoformat())+'.md')

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
                'image': self.image,
                'alt_text': self.altt
            },
            "menu": [
            (
                'menuname': self.menuname,
                'index': self.menuindex
            )
            ]
            "version": __version__
        }

    def write_page(self):

        """
        Writes the dict from header funtion into a file.
        This is our page metadata information.
        """

        with open(self.name, "ab") as f:
            yaml.dump(self.header, f)

    def dump(self):
        """test function"""
        info = yaml.safe_dump(self.header)
        return self.name+'\n'+info


class PagesCreator(PageHeader):

    """
    Subclass of PageHeader for making batch yaml headers and markdown files
    """

    def __init__(self, **kwargs):
        super(PagesCreator, self).__init__(**kwargs)
        self.index = 0
        self.pub = datetime.now()
        self.mod = datetime.now()
        # self.pubdate = self.pub.date().isoformat()
        # self.pubtime = self.pub.time().isoformat()

    def header(self, n):

        """
        Overrides PageHeader's header funtion to one needed for batch creation
        """

        return {
            "title": '',
            "published": self.pub,
            "modified": self.mod,
            "page_type": self.pagetype,
            "book": {
                'title': self.longname,
                'chapter': '',
                'page_number': n,
                'image': '',
                'alt_text': ''
            },
            "menu": [
            (
                'menuname': self.menuname,
                'index': n
            )
            ]
            "version": __version__
        }

    def write_page(self):

        """
        Writes the dict from header funtion into a file.
        This is our page metadata information
        """

        for x in range(1, self.page_amount+1):
            name = os.path.join(self.path, self.shortname+'_'+str(self.index+x)+'.md')
            number = self.index+x
            with open(name, "ab") as f:
                yaml.safe_dump(self.header(number), f)


class PageCreator(PageHeader):

    def __init__(self, **kwargs):
        super(PageCreator, self).__init__(**kwargs)
        self.pub = datetime.now()
        self.mod = datetime.now()
