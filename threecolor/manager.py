import sys
import os
import platform
import click
import yaml

from .application import create_site, page_dir
from .models import pageHeader
from .tools import publish, pagecreator
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

# @cli.command()
# def open():
#     """
#     opens your project folder
#     """
#     pass

@cli.command()
@click.option('--batch', is_flag=True, help='For making more than one new page')
@click.option('--pagetype', prompt='Page type to be created', type=click.Choice(['book', 'news', 'single']))
def newpage(batch, pagetype):

    path = page_dir(pagetype)

    if batch:
        click.echo('batch')
        pamount = click.prompt('Amount of new pages to make')
            
        lname = click.prompt('The title of the Book')
        sname = click.prompt('The shortname of your book (used for filenames)')
        ptype = pagetype
        ptitle = click.prompt('The title of the page')
        pnumber = click.prompt('The number of the page', type=int)
        chptr = click.prompt('The chapter number', type=int)
        img = click.prompt('The name of the image file of your comic page')
        menu = click.prompt('True or False if you want to show up in main menu', type=bool)

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
        print thing.dump(path)


    else:
        lname = click.prompt('The title of the Book')
        sname = click.prompt('The shortname of your book (used for filenames)')
        ptype = pagetype
        ptitle = click.prompt('The title of the page')
        pnumber = click.prompt('The number of the page', type=int)
        chptr = click.prompt('The chapter number', type=int)
        img = click.prompt('The name of the image file of your comic page')
        menu = click.prompt('True or False if you want to show up in main menu', type=bool)

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
        print thing.dump(path)
