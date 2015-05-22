import click
import subprocess
import werkzeug

from datetime import date

from .application import create_site, instfolder
from .tools import publish, misc, pagecreator
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
    click.launch('http://localhost:5001/')
    click.echo('press control+c to stop server')
    app = create_site()
    app.run(debug=True, port=5001)

@cli.command(name='open')
def open_file():
    """Open project folder"""
    click.launch(instfolder)


@cli.command(name='new page')
@click.option('--batch', is_flag=True, help='For making more than one new page')
@click.option('--pagetype', prompt='Page type to be created',
              type=click.Choice(['book', 'news', 'single']), default='book')
def newpage(batch, pagetype):
    """Create a new page"""
    path = misc.page_dir(pagetype)
    pagecreator.new_page(batch, pagetype, path)


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


@cli.command()
@click.option('--foldername', prompt='name of theme to be made',
               default='ThemeName')
def newtheme(foldername):
    """cli call to create a new theme"""
    misc.new_theme(foldername)


# @cli.command(name='setup')
# def make_instance():
#     """Create your Project folder and copy over default config file"""
#     misc.make_home()
