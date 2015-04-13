import sys
import os
import platform
import click

from .application import create_site
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

@cli.command()
@click.option('--batch', is_flag=True, help='For Making more than one new page')
def newpage(batch):
    if batch:
        click.echo('batch')
    else:
        thing=pagecreator.page_creator({shortname='ricks', pagenumber=1})
        thing.print_page
