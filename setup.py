import os
import platform
import subprocess

from setuptools import setup, find_packages

instfolder = os.path.join(os.path.expanduser("~"), '3color-Press')
contfolder = os.path.join(instfolder, 'content')
imgfolder = os.path.join(instfolder, 'images')
themefolder = os.path.join(instfolder, 'themes')
bookfolder = os.path.join(contfolder, 'book')
newsfolder = os.path.join(contfolder, 'news')
singlefolder = os.path.join(contfolder, 'single')

with open('README.txt') as file:
    long_description = file.read()

if platform.system() == 'Windows':

    subprocess.call(
        ['easy_install', "http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win-amd64-py2.7.exe"]
    )

setup(
    name='3color-Press',
    version='0.2.0',
    author='Martin Knobel',
    author_email='mknobel@noties.org',
    license='BSD',
    url='3color.noties.org',
    description='A Flask based static site generator for comics',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        (instfolder, ['threecolor/configs/example.settings.cfg']),
        (imgfolder, []),
        (themefolder, []),
        (contfolder, []),
        (bookfolder, []),
        (newsfolder, []),
        (singlefolder, []),
    ],
    install_requires=[
        'Click',
        'Flask > 0.8',
        'Flask-FlatPages',
        'Frozen-Flask',
        'Fabric'
    ],
    entry_points='''
        [console_scripts]
        3color=threecolor.manager:cli
        ''',

    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)
