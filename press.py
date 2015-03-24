
import sys
import os
import platform

#activate the virtual environment set up by init.py
def activate_venv():
    if platform.system() == 'Windows':
        path = os.path.join(os.getcwd(), 'venv\Scripts\activate_this.py')
        execfile(path, dict(__file__=path))
    else:
        path = os.path.join(os.getcwd(), 'venv/bin/activate_this.py')
        execfile(path, dict(__file__=path))

activate_venv()

import argparse

from threecolor import app, publish

from threecolor.flatpager import chill

from fabric.api import execute

parser = argparse.ArgumentParser(
    prog='3color Press',
    usage='%(prog)s [all | build | compress | publish | run]',
    formatter_class=argparse.RawTextHelpFormatter,
    description= ("""
                    3color Press
        -------------------------------------

        A program to help output your website

        Usage:

            python press.py [ all | build | compress | publish]

        Options:

            all - Builds your site to your build directory and publishes to your remote server

            build - Buids your site to your build directory

            compress - archives your build directory

            publish - pushes your build directory to your remote server

            run - Run your site live, you can browse it by going to localhost:5000 in your browser

    """))


parser.add_argument("options", choices = ['all', 'build', 'compress', 'publish', 'run'],
                    help="type all, build, compress, publish, or run")

args = parser.parse_args()

if args.options == 'all':
    print ("building")
    chill()
    print ("publishing")
    execute(publish.publish)

elif args.options == 'build':
    print ("building")
    chill()

elif args.options == 'compress':
    print ("compressing")
    execute(publish.archive)

elif args.options == 'publish':
    print ("publishing")
    execute(publish.publish)

elif args.options == 'run':
    app.run()

else:
    parser.print_help
