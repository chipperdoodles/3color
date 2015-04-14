import sys
import os
import click

from .application import create_site, page_dir
from .models import pageHeader
from .tools import publish, pagecreator, misc
from .site import coolviews

from fabric.api import execute

@click.group()
def cli():
    pass

@cli.command()
def all():
    """
    Builds your website into Static files and pushes

    is the same as running press build and then press publish
    """
    click.echo('building')
    coolviews.chill()
    click.echo('publishing')
    execute(publish.publish)

@cli.command()
def build():
    """
    Builds website into static files
    """
    click.echo('building')
    coolviews.chill()

@cli.command()
def compress():
    """
    compresses your build folder into a tar.gz file
    """
    click.echo('compressing')
    execute(publish.archive)

@cli.command()
def publish():
    """
    publishes your site according to your configuration
    """
    click.echo('publishing')
    execute(publish.publish)

@cli.command()
def run():
    """
    Runs your website locally in debug mode
    """
    click.echo('running live server at localhost:5000')
    app = create_site()
    app.run()

@cli.command()
def open():
    """
    opens your project folder
    """
    misc.open_browser()

@cli.command()
@click.option('--batch', is_flag=True, help='For making more than one new page')
@click.option('--pagetype', prompt='Page type to be created', type=click.Choice(['book', 'news', 'single']))
def newpage(batch, pagetype):
    """
    Creates a new page, prompting you for information
    """
    path = page_dir(pagetype)

    if batch:
        click.echo('batch')
        pamount = click.prompt('Amount of new pages to make')

        lname = click.prompt('The title of the Book', default=None)
        sname = click.prompt('The shortname of your book (used for filenames)', default=None)
        ptype = pagetype
        ptitle = click.prompt('The title of the page', default=None)
        pnumber = click.prompt('The number of the page', default=None, type=int)
        chptr = click.prompt('The chapter number', default=None, type=int)
        img = click.prompt('The name of the image file of your comic page', default=None)
        menu = click.prompt('True or False if you want to show up in main menu', default=None, type=bool)

        data = dict(
                longname = lname,
                shortname = sname,
                pagetype = ptype,
                pagetitle = ptitle,
                pagenumber = pnumber,
                chapter = chptr,
                image = img,
                menu = menu,
                path = path,
                pamount = page_amount
        )

        thing = pagecreator.pageCreator(**data)
        click.echo(thing.dump())

    else:
        lname = click.prompt('The title of the Book', default=None)
        sname = click.prompt('The shortname of your book (used for filenames)', default=None)
        ptype = pagetype
        ptitle = click.prompt('The title of the page', default=None)
        pnumber = click.prompt('The number of the page', type=int, default=None)
        chptr = click.prompt('The chapter number', type=int, default=None)
        img = click.prompt('The name of the image file of your comic page', default=sname+'_'+str(pnumber)+'.png')
        menu = click.prompt('True or False if you want to show up in main menu', type=bool, default=False)

        data = dict(
                longname = lname,
                shortname = sname,
                pagetype = ptype,
                pagetitle = ptitle,
                pagenumber = pnumber,
                chapter = chptr,
                image = img,
                menu = menu,
                path = path
        )

        thing = pagecreator.pageCreator(**data)
        click.echo(thing.dump())
