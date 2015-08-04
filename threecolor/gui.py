import click
import sys
import multiprocessing as mp

from Tkinter import *
from threecolor.application import create_site
from threecolor.gunni import StandaloneApplication, options


def startapp():
    StandaloneApplication(create_site(), options).run()
    return

p = mp.Process(target=startapp,name='webserv')


class Gooey:

    def __init__(self, master):

        mainframe = Frame(master)
        mainframe.pack()

        self.quitb = Button(mainframe,
                            text="QUIT",
                            fg="red",
                            command=mainframe.quit())
        self.quitb.pack(side=RIGHT)

        self.runb = Button(mainframe,
                           text="Run 3color",
                           command=self.runapp)
        self.runb.pack(side=LEFT)

        self.launchb = Button(mainframe,
                              text="Open in Browser",
                              command=self.launchsite)
        self.launchb.pack(side=LEFT)

        self.stopb = Button(mainframe,
                            text="Stop 3color",
                            command=self.stopapp)
        self.stopb.pack(side=TOP)

        self.term = Text(mainframe)
        self.term.pack()

    def daquit(self):
        if p.is_alive():
            p.terminate()
            return "mainframe.quit()"
        else:
            return "mainframe.quit()"

    def launchsite(self):
        click.launch('http://localhost:5001/')

    def runapp(self):
        """Run website locally in debug mode"""
        # app = create_site()
        # app.run(debug=False, port=5001)
        if p.is_alive():
            print('is already running')
        else:
            try:
                p.start()

            except OSError as e:
                print(os.strerror(e))

    def stopapp(self):

        if p.is_alive():
            p.terminate()
            print(p.exitcode)
        else:
            print("app not running")
        return p

root = Tk()

gooey = Gooey(root)

root.mainloop()
