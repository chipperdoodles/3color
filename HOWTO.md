# How To

In order to make it easier I have included some tools to make it easier to set up the environment.
Currently the application only works in a kind of "manual" mode. That is, if you're going to have to edit some text files and run some command line but it really isn't that hard. It is in a very early version and some things are still broken (for example atom feeds).

To use my init script all you need is to have python on your computer. I have tested it on windows 10 tech preview and Mac Os 10.10.

To OsX comes with Python, Windows users will need to install it.

---
### For windows users:

Fret not, all you have to do is go to python and find the right one, or use this link:
[python.org 2.7.9 amd64 installer](https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi)

Run the Python Installer:

![install for all users](/images/windowspy1.png)

Select Default Path:

![select default path](/images/windowspy2.png)

Change Add python.exe to Path from:

![redx](/images/windowspy3.png)

To this:

![Install local users or add all features](/images/windowspy4.png)
---

#### Download and Extract

Ok now that we've got python for everyone let's start on the fun stuff. Download the project file from [github](https://github.com/chipperdoodles/3color) as a zip (if you use git this is too basic for you and you should know what to do). I suggest extracting the zip file to your home directory. On windows this is `C:\Users\yourusername\` on osX this is `/Users/yourusername/` on linux or bsds this is usually `/home/yourusername/`. So you should now have a folder in your home directory that's named something like 3color-0.1.

#### Gettin Nerdy  
Now we need to get a little nerdy!
Open your terminal (osX) or command prompt (windows) up. You should already be in your home directory, this is the default starting place for your terminal to open and why I suggested extracting the folder there. We need to change to the 3color-0.1 folder, we do this by typing `cd 3color-0.1` and hitting return in terminal.

Now since this is our first time starting the project we need to run init.py. This python script installs all the dependencies needed to run 3color Press. We do this by typing `python init.py` and hitting return in our terminal Wait a while for the script to complete then we'll be ready for the next step.

Once it's finished we're ready to run our press.py script! Try typing `python press.py run` and hitting enter in terminal, this will run our website locally and live so we can see any changes we make and get an idea on what it looks like. (currently the default code might break because of an atom error, i'm going to comment it out of the master-branch soon so people can toy around with it).

Oops! where's the content? you'll notice your site is pretty blank. You're installed and ready to use 3color press, but we don't have any content in the instance/content folder. I've included some basic static pages but you'll need to get making your own!

####Configuration
if you took a look at the files you'll notice there's a settings.cfg, open it up in a text editor and fill out the values you need, it is explained in the file. If you make any changes to the settings file while your the local server is running (see end of making content `python press.py run` )

#### Making Content
Ok, I mentioned doing things manually, this is pretty much making text files in markdown format with correctly filled header info and putting them in the right folder.

There are 3 different page types by default. These are book pages, news pages, and single_pages. Book pages include auto page navigation according to what their book title and page number are. News pages are organized by published date and can be found in the /news/ route, but also put into a feed if you choose to custom theme them. Single Page pages are pages to hold site information, such as contact, about me, or any custom one off page you may want.

Default text editors are kind of terrible, I would suggest using something free [Atom](https://atom.io/), [Brackets](http://brackets.io/) which are free and powerful or simple options like [Text Wrangler](http://www.barebones.com/products/textwrangler/download.html) or [Notepad ++](http://notepad-plus-plus.org/), or some even editors like [sublime text](http://macromates.com/), [textmate](http://macromates.com/), which may cost money and are potentially overkill but are pretty nice. If you're feeling especially nerdy on unix-like systems you can look into the command line tools like [nano](http://www.nano-editor.org/), [vim](http://www.vim.org/), or [emacs](https://www.gnu.org/software/emacs/) to edit your files, never having to leave the terminal!

so now we need to make our files! it is very simple.

open up our text file and and create a file that looks like this:


      title: ""
      published: yyyy-mm-dd
      modified: yyyy-mm-dd
      page_type:
      book: { 'title': "", 'chapter': '' , 'page_number': '', 'image': ""}
      menu:
      version: 0.1


* title is the title of the page, it shows up on the webpage.
* published is the date you post it in yyyy-mm-dd
* modified is the date if you want to post changes to the file. Not currently used, in here as a just in case, fill in the value of the published date
* page_type is the type of this page. Available choices are: book, news, single_page. note that the files must be saved in the appropriate directory. book in your content/books directory, news in your content/instance directory, single_page in your content/single_page dir.
* book: is where you fill out info for your book pages. Title is book title, chapter is chapter number, page_number is the page number and image is the name of your comic image file uploaded in your instance/images folder. (chapter and page_number are integers and image has to include your filename extension such as .png or .jpg)
* menu is a True or False statement. If marked true and entry for this page will be automatically added to the main menu
* version is 0.1 for now and represents the version of 3color the file was built with, hopefully making migration easier if there are bigger changes

book page example (note: For comic pages you don't need anything after the option menu):


      title: "Ricks Page 3"
      published: 2016-02-18
      modified: 2016-02-18
      page_type: book
      book: { 'title': "Ensign Ricks", 'chapter': 2, 'page_number': 3, 'image': "rick_15.png" }
      menu: False
      version: 0.1


news and single_page example (note: for these pages you need a return after menu follwed by content written in markdown, which will be rendered into an html page)


      title: "Contact"
      published: 2016-03-01
      page_type: single_page
      book: { 'title': "", 'chapter': '', 'page_number': '', 'image': "" }
      menu: True
      version: 0.1

      If you need to reach me you can find me on the [tweeters](https://twitter.com/chipperdoodles)

Save the files appropriately and you'll have content! If we try our `python press.py run` and visit localhost:5000 we'll see our new pages!
If you left `python press.py run` running in terminal then it should auto reload and you should see the new pages


#### Building

Time to build! Well this tool isn't meant to run live production sites, instead it's meant to take that live site and build it into a bunch of static html files. We can do this very simply run `python press.py build`. This builds the folder into whatever you configured it to in the instance/ folder. Default is build. This folder will contain your website! You can now upload this to your web server and you should be good to go.

Luckily 3color has included some built in tools that allow you to push your website to a remote server. Right now you need to have ssh or sftp access to your remote server. Git is also supported if you have it (check out threecolor/publish.py to see how it pushes with git).

#### Publishing

Okay! we built it! all we have to do to publish is `python press.py publish` and it will push your site according to the method you configure. That's it! Support for normal ftp will be looked into and probably added. If you want to do it yourself you can compress your site into an archive by running `python press.py compress`. This does the same thing as it would if you set your PUB_METHOD to 'local' and ran `python press.py publish`.

to save yourself some time you can run `python press.py all` and this will run the build command follwed by the publish command.

#### Theming

Currently I am working on building a default theme for the website. Right now the css is just demo css to show off some of the containers and regions. If you know a little css, feel free to dig around threecolor/static/css and edit and format. I will be looking into adding theming support so you won't have to worry about breaking things as time progresses. Since this is a very early version things will change. If you feel brave enough you can dip into the threecolor/templates folder and change the jinja themeing around. There's a lot you can do with themeing and if you know html, [jinja](http://jinja.pocoo.org/) is not terrible to understand.
