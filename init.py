# Script to set up virtual environment and install dependencies

import os
import platform
import subprocess

system = platform.system()

# TODO: is this file superceded by setup.py?
# if this file is not superceded by setup.py, note that the
# pip install calls below will not work when called from
# system python instance (requires sudo)


# installs app dependencies with pip
def install_depends():
    subprocess.call(['pip', 'install', 'Flask', 'Flask-FlatPages', 'Frozen-Flask', 'Fabric'])


# installs virtual environment to global python python packages
def install_venv():
    subprocess.call(['pip', 'install', 'virtualenv'])


# creates a folder named venv in project directory and installs a virtual environment into it
def create_venv():
    path = os.path.join(os.getcwd(), 'venv')
    subprocess.call(['virtualenv', path])


# main installs all dependencies to the created virtual enviromment according to operating system
def system_install():
    if system == 'Windows':
        path = os.path.join(os.getcwd(), 'venv', 'scripts', 'activate_this.py')
        with open(path) as f:
            code = compile(f.read(), path, 'exec')
            exec(code, globals(), locals())
        subprocess.call(
            ['easy_install', "http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win-amd64-py2.7.exe"]
        )
        install_depends()
    else:
        path = os.path.join(os.getcwd(), 'venv', 'bin', 'activate_this.py')
        with open(path) as f:
            code = compile(f.read(), path, 'exec')
            exec(code, globals(), locals())
        install_depends()

if __name__ == "__main__":
    install_venv()
    create_venv()
    system_install()
