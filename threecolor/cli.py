import click
import subprocess
import os

from .application import create_site, instfolder, active_sitefolder
from .tools import publish, misc, pagecreator
from .site import coolviews
from .configs import conf

try:
    from flask_debugtoolbar import DebugToolbarExtension
except:
    pass

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
               this will call on atom to open your project folder

    \b
    new-page    Creates a new page (.md file) based on your inputs.
               You can pass the option --batch in order to created a batch of pages
               with auto page numbering and file naming.
                \b
                  example: 3color newpage --batch
    \b
    new-theme   Creates a theme of your name choice in the themes folder
               and copies over the default theme files and to help quick start themeing.
               Prompts user for name of folder for the new theme.
    \b
    new-site    Creates a folder for a new site. If you want to work on this site
               remember to edit sites.cfg in your project folder

    \b
    run        Runs your website locally on port 5000 and opens http://localhost:5000
               in your default web browser. Use this command in order to see
               what your website will look like before you build it. Useful for
               Theme building. Press contrl+c to halt the live server.
               Use with --debug to run server in debug mode.

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
@click.option('--pubmethod',
              type=click.Choice(['sftp', 'rsync', 'local', 'git']))
def push_site(pubmethod):
    """Publish site to remote server"""
    click.echo('publishing')
    if pubmethod:
        publish.publish(pubmethod)
    else:
        publish.publish()


# FIXME launches multiple browser windows/tabs if flask is reloaded from debug
@cli.command(name='run')
@click.option('--debug', is_flag=True)
def run_server(debug):
    """Run website locally in debug mode"""
    # click.echo('press control+c to stop server')
    # click.launch('http://localhost:5001/')
    app = create_site()
    if debug:
        app.config['SECRET_KEY']= 'nope'
        toolbar = DebugToolbarExtension(app)
        app.run(debug=True, port=5001)
    else:
        app.run(debug=True, port=5001)


@cli.command(name='open')
def open_file():
    """Open project folder"""
    click.launch(instfolder)


@cli.command(name='new-page')
@click.option('--batch', is_flag=True, help='For making more than one new page')
@click.option('--pagetype', prompt='Type of page to be created ',
              type=click.Choice(['book', 'news', 'single', 'gallery']),
              default='book')
def newpage(batch, pagetype):
    """Create a new page"""
    path = misc.page_dir(pagetype)
    pagecreator.new_page(batch, pagetype, path)


@cli.command()
def atom():
    """Open project folder with atom editor"""
    try:
        if misc.system == 'Windows':
            subprocess.check_call(["atom", instfolder], shell=True)
        else:
            subprocess.check_call(["atom", instfolder])

    except OSError as e:
        print(os.strerror(e))
        print("The atom editor command line tool not installed")


@cli.command(name='new-theme')
@click.option('--foldername', prompt='name of theme to be made',
              default='ThemeName')
def newtheme(foldername):
    """Create a new theme"""
    misc.new_theme(foldername)


@cli.command(name='new-site')
@click.option('--foldername', prompt='name of theme to be made',
              default='Site Name')
def newsite(foldername):
    """Create a new site"""
    misc.new_site(foldername)

#to do, make more in depth set up process
@cli.command(name='setup')
def upconfig():
    """Copy over default config file, open in editor"""

    cf = os.path.join(active_sitefolder, 'settings.cfg')

    if conf.cfg_check(cf):
        click.edit(filename=cf)
    else:
        misc.copy_config()
