import click

from datetime import date

from ..models import PagesCreator, PageCreator

up = click.UNPROCESSED


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
        pnumber = click.prompt('The number of the page', type=int)
        ptitle = click.prompt('The title of the page',
                              default=lname+' '+'Page: '+str(pnumber))
        chptr = click.prompt('The chapter number', type=int)
        img = click.prompt('The name of the image file of your comic page',
                           default=sname+'_'+str(pnumber)+'.png', type=up)
        menu = click.prompt('Name of the menu this page belongs to',
                            type=up, default='main-menu')

        data = {
            "longname": lname,
            "shortname": sname,
            "pagetype": ptype,
            "pagetitle": ptitle,
            "pagenumber": pnumber,
            "chapter": chptr,
            "image": img,
            "menuname": menu,
            "menuindex": pnumber,
            "path": path
        }

        thing = PageCreator(**data)
        thing.write_page()

    else:
        ptype = pagetype
        sname = click.prompt('The shortname used for filenames, example: news',
                             default='news', type=up)
        ptitle = click.prompt('The title of the page',
                              type=up,
                              default=sname+" "+str(date.today()))
        menu = click.prompt('Name of the menu this page belongs to',
                            type=up, default='main-menu')
        index = click.prompt('Weight of item, used for the order of the menu',
                             type=int, default='')

        data = {
            "longname": None,
            "shortname": sname,
            "pagetype": ptype,
            "pagetitle": ptitle,
            "pagenumber": None,
            "chapter": None,
            "image": None,
            "menuname": menu,
            "menuindex": index,
            "path": path
        }

        edit = click.prompt('would you like to edit the page now? (yes|no)',
                            type=bool, default='yes')

        if edit:
            print("opening file to edit")

        thing = PageCreator(**data)
        thing.write_page()
