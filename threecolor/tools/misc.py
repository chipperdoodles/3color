import os
import subprocess
import shutil

from ..configs import sysinfo, config

instfolder = config.instfolder

inst_dir_list = ['content', 'images', 'themes']

content_dir_list = ['book', 'news', 'single']


def open_browser():
    if sysinfo.system == 'Windows':
        os.startfile(instfolder['open'])
    elif sysinfo.system == 'Darwin':
        subprocess.call(["open", instfolder])
    else:
        try:
            subprocess.call(['xdg-open', instfolder])
        except OSError:
            print("Operating system doesn't have lazy file browser opener")

def make_home(root_path):

    if os.path.exists(instfolder):
        print("3color Press folder already exists")

    else:
        os.mkdir(instfolder)
        shutil.copyfile(os.path.join(root_path, 'configs', 'example.settings.cfg'), os.path.join(instfolder, 'settings.cfg'))

        for folder in inst_dir_list:
            os.mkdir(os.path.join(instfolder, folder))

        for folder in content_dir_list:
            os.mkdir(os.path.join(instfolder, 'content', folder))
