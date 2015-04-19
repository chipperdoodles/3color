import os
import subprocess
import shutil
import platform

from ..configs import config

instfolder = config.instfolder

system = platform.system()


def page_dir(dirname):
    """used in command line tools to determine path for content type"""
    ptype_dir = os.path.join(instfolder, 'content', dirname)
    return ptype_dir


def open_browser():
    """
    Try's to open system's file browser.

    Currently the command line tool uses click.launch but this
    may be used for future admin interface
    """
    if system == 'Windows':
        os.startfile(instfolder['open'])
    elif system == 'Darwin':
        subprocess.call(["open", instfolder])
    else:
        try:
            subprocess.call(['xdg-open', instfolder])
        except OSError:
            print("Operating system doesn't have lazy file browser opener")


def make_home(root_path):
    """
    This function looks for the user's 3color-Press folder (instance folder)
    and creates one if it doesn't exist. Currently not in use
     """
    inst_dir_list = ['content', 'images', 'themes']
    content_dir_list = ['book', 'news', 'single']

    if os.path.exists(instfolder):
        print("3color-Press folder already exists")

    else:
        os.mkdir(instfolder)
        shutil.copyfile(os.path.join(root_path, 'configs', 'example.settings.cfg'),
                        os.path.join(instfolder, 'settings.cfg'))

        for folder in inst_dir_list:
            os.mkdir(os.path.join(instfolder, folder))

        for folder in content_dir_list:
            os.mkdir(os.path.join(instfolder, 'content', folder))
