import click
import subprocess

from .application import create_site, page_dir, instfolder
from .tools import publish, misc
from .models import PagesCreator, PageCreator
from .site import coolviews

# TODO: make fabric optional
from fabric.api import execute


@click.group()
def cli():
    """ 3color Press command line tool

    This provides command line tools to manage your 3color site.
    Simply pass a command after 3color to get something done!

    Options:

    build - Builds your website into static files located in your configured build directory.
    The default build directory is instance/build

    compress - Archives your build directory into a tar.gz file

    publish - Pushes your website to your remote server depending on your configuration

    all - Builds and then Publishes your website. This is the same as running '3color build'
    and then '3color publish'

    open - Opens the project folder in your file browser

    newpage - creates a new page based on your given inputs. Accepts the option --batch.
    If you declare --batch then it will ask for page amount and create files with empty templates as neccesary.
    example usage: '3color newpage --batch' or '3color newpage'

    """
    pass


@cli.command(name='all')
def build_push():  # FIXME: shadows builtin all()
    """ Builds your website into Static files and pushes

    is the same as running press build and then press publish
    """
    click.echo('building')
    coolviews.chill()
    click.echo('publishing')
    execute(publish.publish)


@cli.command()
def build():
    """Builds website into static files"""
    click.echo('building')
    coolviews.chill()


@cli.command()
def compress():
    """compress your build folder into a tar.gz file"""
    click.echo('compressing')
    execute(publish.archive)


@cli.command()
def publish():
    """publish your site according to your configuration"""
    click.echo('publishing')
    execute(publish.publish)


@cli.command()
def run():
    """Run website locally in debug mode"""
    click.echo('running live server at localhost:5000')
    app = create_site()
    app.run()


@cli.command(name='open')
def open_file():  # FIXME: shadows builtin open()
    """open your project folder"""
    misc.open_browser()


@cli.command()
@click.option('--batch', is_flag=True, help='For making more than one new page')
@click.option('--pagetype', prompt='Page type to be created', type=click.Choice(['book', 'news', 'single']), default='book')
def newpage(batch, pagetype):
    """Creates a new page, prompting you for information"""
    path = page_dir(pagetype)

    if batch:
        pamount = click.prompt('Amount of new pages to make', type=int)

        lname = click.prompt('The title of the Book', default='')
        sname = click.prompt('The shortname of your book (used for filenames)', default='')
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

    else:
        lname = click.prompt('The title of the Book', default='')
        sname = click.prompt('The shortname of your book (used for filenames)', default='')
        ptype = pagetype
        ptitle = click.prompt('The title of the page', default='')
        pnumber = click.prompt('The number of the page', type=int)
        chptr = click.prompt('The chapter number', type=int)
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
        thing.write_page()


@cli.command()
def atom():
    """Calls the atom Command line tool to open """
    try:
        subprocess.call(['atom', instfolder])
    except OSError:
        print("The atom editor command line tool not installed")
