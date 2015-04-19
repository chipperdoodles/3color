import os
import subprocess

from ..application import create_site
from ..configs import config

# TODO: make fabric optional
from fabric.api import *
from fabric.api import execute
from fabric.contrib.project import rsync_project
from fabric.contrib.files import exists

from shutil import make_archive

instfolder = config.instfolder

cfg = config.make_usr_cfg()

# configure user and hostname for remote server
env.user = cfg['USER_NAME']
env.hosts = cfg['REMOTE_SERVER']
pub_method = cfg['PUB_METHOD']
build_dir = cfg['FREEZER_DESTINATION']


def archive():
    """
    Makes a local tar.gz file
    """
    make_archive(os.path.join(instfolder, '3colorSite'), 'gztar', build_dir)


def rsync():
    """
    Uses a wrapper to call rsync to deploy your site with the rsync tool
    this has the delete option which will delete any remote files that are
    not in your local build folder
    """
    local = os.path.join(instfolder, build_dir+'/')
    remote = '3colorsite/'
    rsync_project(remote, local, delete=True)


# TODO test functionality
def git_deploy():
    """
    simply changes the directory to your build directory and calls
    git commits to add all files, commit all changes with commit message updated
    and then push your commit, then change back to your project directory
    """
    project = os.getcwd()
    local = os.path.join(instfolder, build_dir)
    os.chdir(local)
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'commit', '-a', '-m', 'updated'])
    subprocess.call(['git', 'push'])
    os.chdir(project)


# TODO: make nicer, add non-fabric plain FTP support
def sftp():
    """
    archives then uploads site via fabric sftp and then unarchives on server.
    The remote folder for your site will be 3colorsite and contents will be deleted
    if the directory exists remotely therefore ensuring to remove changes before the upload
    """
    make_archive(os.path.join(instfolder, '3colorSite'), 'gztar', build_dir)
    tarfile = os.path.join(instfolder, '3colorSite.tar.gz')

    if exists('~/3colorSite'):
        run('rm -rf ~/3colorSite/*')
        put(tarfile, '~/3colorSite/3colorSite.tar.gz')
        with cd('~/3colorSite/'):
            run('tar xzf 3colorSite.tar.gz')
            run('rm -rf 3colorSite.tar.gz')
    else:
        run('mkdir ~/3colorSite')
        put(tarfile, '~/3colorSite/3colorSite.tar.gz')
        with cd('~/3colorSite/'):
            run('tar xzf 3colorSite.tar.gz')
            run('rm -rf 3colorSite.tar.gz')

    os.remove(tarfile)


def publish(pubmethod=pub_method):
    """Main function to pubish site"""
    if pubmethod == 'sftp':
        execute(sftp)

    elif pubmethod == 'rsync':
        execute(rsync)

    elif pubmethod == 'git':
        git_deploy()

    elif pubmethod == 'local':
        archive()

    else:
        print("You did not configure your publish method")
