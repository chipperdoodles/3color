import click
import subprocess

from datetime import date

from .application import create_site, instfolder
from .tools import publish, misc
from .models import PagesCreator, PageCreator
from .site import coolviews

up = click.UNPROCESSED


@click.group()
def cli():
    """ 3color Press command line tool

    This provides command line tools to manage your 3color site.
    Simply pass a command after 3color to get something done!
    The project folder is the 3color-Press folder in your home directory.

    Commands available:

    \b
    build      Builds your website as static html to your build folder.
               The default build folder is 'build' in your project folder

    \b
    compress   Archives your build directory into a tar.gz file.
               Does the same as if your PUB_METHOD is local

    \b
    publish    Pushes your website to your remote server. It will use configured
               PUB_METHOD by default unless you supply --pubmethod option.
               Using --pubmethod will override your default method and must be one
               of these options: sftp, rsync, local, or git.
               \b
                 example: 3color publish --pubmethod rysnc

    \b
    all        Builds and then publishes your website.
               This is the same as running '3color build' and then '3color publish'

    \b
    open       Opens the project folder in your file browser

    \b
    atom       If you have the Atom Editor installed,
               this will call on atom to open your project folder in atom

    \b
    newpage    Creates a new page (.md file) based on your inputs.
               You can pass the option --batch in order to created a batch of pages
               with auto page numbering and file naming.
                \b
                  example: 3color newpage --batch
    \b
    run        Runs your website locally on port 5000 and opens http://localhost:5000
               in your default web browser. Use this command in order to see
               what your website will look like before you build it. Useful for
               Theme building. press contrl+c to halt the live server.

    """
    pass


@cli.command(name='all')
def build_push():
    """Builds and then publishes your website."""
    click.echo('building to build folder')
    app = create_site()
    coolviews.chill()
    click.echo('publishing with default pub method')
    publish.publish


@cli.command()
def build():
    """Builds website into static files"""
    click.echo('building')
    app = create_site()
    coolviews.chill()


@cli.command()
def compress():
    """Compress build folder into a tar.gz file"""
    click.echo('compressing')
    execute(publish.archive)


@cli.command(name='publish')
@click.option('--pubmethod', type=click.Choice(['sftp', 'rsync', 'local', 'git' ]))
def push_site(pubmethod):
    """Publish site to remote server"""
    click.echo('publishing')
    if pubmethod:
        publish.publish(pubmethod)
    else:
        publish.publish()


# FIXME launches browser windows
@cli.command()
def run():
    """Run website locally in debug mode"""
    click.launch('http://localhost:5000/')
    app = create_site()
    app.run()


@cli.command(name='open')
def open_file():
    """Open project folder"""
    click.launch(instfolder)


@cli.command()
@click.option('--batch', is_flag=True, help='For making more than one new page')
@click.option('--pagetype', prompt='Page type to be created',
              type=click.Choice(['book', 'news', 'single']), default='book')
# TODO: Create pagetype specific forms
def newpage(batch, pagetype):
    """Create a new page"""
    path = misc.page_dir(pagetype)

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

    else:
        lname = click.prompt('The title of the Book', default='', type=up)
        sname = click.prompt('The shortname of your book (used for filenames)',
                             default='', type=up)
        ptype = pagetype
        ptitle = click.prompt('The title of the page',
                              default='{:%Y-%m-%d}'.format(date.today()))
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


@cli.command()
def atom():
    """ Open project folder with atom editor"""
    try:
        if misc.system == 'Windows':
            subprocess.check_call(["atom", instfolder], shell=True)
        else:
            subprocess.check_call(["atom", instfolder])

    except OSError as e:
        print(os.strerror(e))
        print("The atom editor command line tool not installed")


# @cli.command(name='setup')
# def make_instance():
#     """Create your Project folder and copy over default config file"""
#     misc.make_home()
