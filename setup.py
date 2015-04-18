import platform
import subprocess

from setuptools import setup, find_packages

with open('README.txt') as file:
    long_description = file.read()

if platform.system() == 'Windows':

    subprocess.call(
        ['easy_install', "http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win-amd64-py2.7.exe"]
    )

setup(
    name='threecolor',
    version='0.2.0',
    author='Martin Knobel',
    author_email='mknobel@noties.org',
    url='3color.noties.org',
    description='A Flask based static site generartor for comics',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Flask',
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
        'Intended Audience :: End Users/Desktop',
        'Topic :: Web',
    ]
)
