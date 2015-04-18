import os
import subprocess

from ..configs import sysinfo
from ..application import instfolder


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
