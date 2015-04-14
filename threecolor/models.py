import os
import sys
import yaml
from . import __version__
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
