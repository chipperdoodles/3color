import os
import sys

class page_header(object):

    def __init__(self, **kwargs):

        self.longname = 'longname'
        self.pagetype = 'pagetype'
        self.pageamount = 'pageamount'
        self.pagetitle = 'pagetitle'
        self.pagenumber = 'pagenumber'
        self.published = 'pub'
        self.modified = 'mod'
        self.image = 'image'
        self.menu = 'menu'

        for 

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
