import os
import sys

class page_header(object):

    def __init__(self, **kwargs):

        shortname = self.shortname
        longname = self.longname
        pagetype = self.pagetype
        pageamount = self.pageamount
        pagetitle = self.pagetitle
        pagenumber = self.pagenumber
        pub = self.published
        mod = self.modified
        image = self.image
        menu = self.menu

    def header():

        header = dict(
            title = pagetitle,
            published = pub,
            modified = mod,
            page_type = pagetype,
            book = {'title': longname, 'chapter': chapter, 'page_number': pagenumber, 'image': image},
            menu = menu,
            version = __version__ )

        return header
