import sys  # FIXME: unused import
import subprocess

from ..configs import sysinfo
from ..application import instfolder
from os import startfile  # FIXME: not python3 friendly

def open_browser():
    if sysinfo.system=='Windows':
        startfile(instfolder['open'])
    elif sysinfo.system=='Darwin':
        subprocess.call(["open", instfolder])
    else:
        try:
            subprocess.call(['xdg-open', instfolder])
        except OSError:
            print('Operating system doesn\'t have lazy file browser opener')
