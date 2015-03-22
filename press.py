import sys
import os
import argparse

from threecolor import app
from threecolor import publish
from fabric.api import execute
from flask_frozen import Freezer

freezer = Freezer(app)
parser = argparse.ArgumentParser()


parser.add_argument("options", choices = ['all', 'build', 'compress', 'publish', 'run'],
                    help="type all, build, compress, publish, or run")

args = parser.parse_args()

if args.options == 'all':
    print ("building")
    freezer.freeze()
    print ("publishing")
    execute(publish.publish)

elif args.options == 'build':
    print ("building")
    freezer.freeze()

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
