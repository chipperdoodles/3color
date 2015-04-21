Command Line Tool
================

3color-Press provides a command line tool for managing your site.
After install you can simply type 3color --help to see if it's installed and accessible

Commands
--------

from 3color --help: ::

  (env1)$ 3color --help
  Usage: 3color [OPTIONS] COMMAND [ARGS]...

    3color Press command line tool

    This provides command line tools to manage your 3color site. Simply pass a
    command after 3color to get something done! The project folder is the
    3color-Press folder in your home directory.

    Commands available:

    build      Builds your website as static html to your build folder.
               The default build folder is 'build' in your project folder

    compress   Archives your build directory into a tar.gz file.
               Does the same as if your PUB_METHOD is local

    publish    Pushes your website to your remote server. It will use configured
               PUB_METHOD by default unless you supply --pubmethod option.
               Using --pubmethod will override your default method and must be one
               of these options: sftp, rsync, local, or git.

                 example: 3color publish --pubmethod rysnc

    all        Builds and then publishes your website.
               This is the same as running '3color build' and then '3color publish'

    open       Opens the project folder in your file browser

    atom       If you have the Atom Editor installed,
               this will call on atom to open your project folder in atom

    newpage    Creates a new page (.md file) based on your inputs.
               You can pass the option --batch in order to created a batch of pages
               with auto page numbering and file naming.

                  example: 3color newpage --batch

    run        Runs your website locally on port 5000 and opens http://localhost:5000
               in your default web browser. Use this command in order to see
               what your website will look like before you build it. Useful for
               Theme building. press contrl+c to halt the live server.

  Options:
    --help  Show this message and exit.

  Commands:
    all       Builds and then publishes your website.
    atom      Open project folder with atom editor
    build     Builds website into static files
    compress  Compress build folder into a tar.gz file
    newpage   Create a new page
    open      Open project folder
    publish   Publish site to remote server
    run       Run website locally in debug mode
