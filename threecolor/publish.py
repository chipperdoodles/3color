import os
import subprocess

from threecolor import app
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib.files import exists
from shutil import make_archive

env.user = app.config['USER_NAME']
env.hosts = app.config['REMOTE_SERVER']

def archive():
    """
    Makes a local tar.gz file
    """
    make_archive('threecolorSite', 'gztar', app.config['BUILD_DIR'])

def uptime():
    """
    runs the uptime command on remote server
    currently here just to test functionality
    """
    run("uptime")

def rsync():
    """
    Uses a wrapper to call rsync to deploy your site with the rsync tool
    this has the delete option which will delete any remote files that are
    not in your local build folder
    """
    local = os.path.join(os.getcwd(), app.config['BUILD_DIR']+'/')
    remote = app.config['REMOTE_SERVER']
    rsync_project(remote, local, delete=True)

def git_deploy():
    project = os.getcwd()
    local = os.path.join(app.instance_path, app.config['BUILD_DIR'])
    os.chdir(local)
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'commit', '-a', '-m', 'updated'])
    subprocess.call(['git', 'push'])
    os.chdir(project)

def upload():
    """
    archives then uploads site via fabric sftp and then unarchives on server.
    The remote folder for your site will be threecolor and contents will be deleted if
    the directory exists remotely therefore ensuring to remove any site changes before the upload
    """
    make_archive('threecolorSite', 'gztar', app.config['BUILD_DIR'])

    if exists('~/threecolor'):
        run('rm -rf ~/threecolor/*')
        put('threecolorSite.tar.gz', '~/threecolor/threecolor.tar.gz')
        with cd('~/threecolor/'):
            run('tar xzf threecolor.tar.gz')
            run('rm -rf threecolor.tar.gz')
    else:
        run('mkdir ~/threecolor')
        put('threecolorSite.tar.gz', '~/threecolor/threecolor.tar.gz')
        with cd('~/threecolor/'):
            run('tar xzf threecolor.tar.gz')
            run('rm -rf threecolor.tar.gz')

    local('rm -rf threecolorSite.tar.gz')

def publish():
    if app.config['PUB_METHOD'] == 'sftp':
        upload()
    elif app.config['PUB_METHOD'] == 'rsync':
        rsync()
    elif app.config['PUB_METHOD'] == 'git':
        git_deploy()
    elif app.config['PUB_METHOD'] == 'local':
        archive()
    else:
        print "You did not configure your publish method"
