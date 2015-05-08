import click

from datetime import date

from ..models import PagesCreator, PageCreator
from . import misc

up = click.UNPROCESSED

# TODO: Create pagetype specific forms
def new_page(batch, pagetype, path):

    if batch:
        pamount = click.prompt('Amount of new pages to make', type=int)

        lname = click.prompt('The title of the Book', default='', type=up)
        sname = click.prompt('The shortname of your book (used for filenames)',
                             default='', type=up)
        ptype = pagetype

        data = dict(
                longname=lname,
                shortname=sname,
                pagetype=ptype,
                path=path,
                page_amount=pamount
        )

        thing = PagesCreator(**data)
        thing.write_page()


    elif pagetype == 'book':
        lname = click.prompt('The title of the Book', default='', type=up)
        sname = click.prompt('The shortname of your book (used for filenames)',
                             default='', type=up)
        ptype = pagetype
        ptitle = click.prompt('The title of the page',
                              default=date.today())
        pnumber = click.prompt('The number of the page', type=int)
        chptr = click.prompt('The chapter number', type=int)
        img = click.prompt('The name of the image file of your comic page',
                           default=sname+'_'+str(pnumber)+'.png', type=up)
        menu = click.prompt('True or False for link in main menu',
                            type=bool, default=False)

        data = {
            "longname": lname,
            "shortname": sname,
            "pagetype": ptype,
            "pagetitle": ptitle,
            "pagenumber": pnumber,
            "chapter": chptr,
            "image": img,
            "menu": menu,
            "path": path
        }

        thing = PageCreator(**data)
        thing.write_page()


    else:
        ptype = pagetype
        sname = click.prompt('The shortname used for filenames, example: news',
                              default='news', type=up)
        ptitle = click.prompt('The title of the page',
                              default=date.today())
        menu = click.prompt('True or False for link in main menu',
                            type=bool, default=False)

        data = {
            "longname": None,
            "shortname": sname,
            "pagetype": ptype,
            "pagetitle": ptitle,
            "pagenumber": None,
            "chapter": None,
            "image": None,
            "menu": menu,
            "path": path
        }

        thing = PageCreator(**data)
        thing.write_page()
