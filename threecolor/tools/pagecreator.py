import click

from ..models import PagesCreator, PageCreator
from ..application import page_dir
from ..manager import cli

# TODO currently file is not used


@cli.command()
@click.option('--batch', is_flag=True, help='For making more than one new page')
@click.option('--pagetype', prompt='Page type to be created', type=click.Choice(['book', 'news', 'single']))
def newpage(batch, pagetype):
    """Creates a new page, prompting you for information"""
    path = page_dir(pagetype)

    if batch:
        pamount = click.prompt('Amount of new pages to make', type=int)

        lname = click.prompt('The title of the Book', default=None)
        sname = click.prompt('The shortname of your book (used for filenames)', default='')
        ptype = pagetype

        data = {
            "longname": lname,
            "shortname": sname,
            "pagetype": ptype,
            "path": path,
            "page_amount": pamount
        }

        thing = PagesCreator(**data)
        thing.write_page()

    else:
        lname = click.prompt('The title of the Book', default='')
        sname = click.prompt('The shortname of your book (used for filenames)', default='')
        ptype = pagetype
        ptitle = click.prompt('The title of the page', default=None)
        pnumber = click.prompt('The number of the page', type=int, default=None)
        chptr = click.prompt('The chapter number', type=int, default=None)
        img = click.prompt('The name of the image file of your comic page', default=sname+'_'+str(pnumber)+'.png')
        menu = click.prompt('True or False if you want to show up in main menu', type=bool, default=False)

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
        click.echo(thing.dump())
