import os
import subprocess
import shutil
import platform

from ..configs import conf

instfolder = conf.instfolder
active_sitefolder = conf.active_sitefolder
default_site_folder = os.path.join(instfolder, 'sites', 'default')
root_path = os.path.dirname(conf.APP_ROOT)
system = platform.system()


def page_dir(dirname):
    """
    used in command line tools to determine path for content type
    """
    ptype_dir = os.path.join(active_sitefolder, 'content', dirname)
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
        os.mkdir(instfolder, 'sites')
        os.mkdir(default_site_folder)
        shutil.copyfile(os.path.join(root_path, 'configs', 'example.settings.cfg'),
                        os.path.join(default_site_folder, 'settings.cfg'))

        for folder in inst_dir_list:
            os.mkdir(os.path.join(default_site_folder, folder))

        for folder in content_dir_list:
            os.mkdir(os.path.join(default_site_folder, 'content', folder))


def new_theme(foldername='CHANGE_MY_NAME'):
    """
    This function copies the default theme files to the theme's folder of a user's
    project folder.
    """
    os.mkdir(os.path.join(default_site_folder, 'themes', foldername))
    shutil.copyfile(os.path.join(rooth_path, 'configs', 'default_template_settings.py'),
                    os.path.join(default_site_folder, 'themes', foldername, 'theme_settings.cfg'))
    shutil.copytree(os.path.join(root_path, 'site', 'templates'),
                    os.path.join(default_site_folder, 'themes', foldername, 'templates'))
    shutil.copytree(os.path.join(root_path, 'site', 'static'),
                    os.path.join(default_site_folder, 'themes', foldername, 'static'))


def copy_config():
    shutil.copyfile(os.path.join(root_path, 'configs', 'example.settings.cfg'),
                    os.path.join(active_sitefolder, 'settings.cfg'))
    shutil.copyfile(os.path.join(root_path, 'configs', 'default_sites.py'),
                    os.path.join(instfolder, 'sites.cfg'))

def new_site(foldername='CHANGE_MY_NAME'):

    inst_dir_list = ['content', 'images', 'themes']
    content_dir_list = ['book', 'news', 'single', 'gallery']
    newfold = os.path.join(instfolder, 'sites', foldername)

    if os.path.exists(newfold):
        print('Folder with that name already exists')
    else:
        os.mkdir(newfold)

        for folder in inst_dir_list:
            os.mkdir(os.path.join(newfold, folder))

        for folder in content_dir_list:
            os.mkdir(os.path.join(newfold, 'content', folder))
