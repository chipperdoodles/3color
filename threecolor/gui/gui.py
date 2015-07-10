import click
import multiprocessing as mp

from Tkinter import Frame, Tk, Button, LEFT, TOP, RIGHT
from threecolor.application import create_site
from threecolor.gunni import StandaloneApplication, options


def startapp():
    StandaloneApplication(create_site(), options).run()
    return

p = mp.Process(target=startapp)


class Gooey:

    def __init__(self, master):

        mainframe = Frame(master)
        mainframe.pack()

        self.quitb = Button(mainframe,
                            text="QUIT",
                            fg="red",
                            command=self.daquit)
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
            print("app already running")
        else:
            try:
                p.start()
            except:
                print("oops")

    def stopapp(self):

        if p.is_alive():
            p.terminate()
        else:
            print("app not running")
        return p

root = Tk()

gooey = Gooey(root)

root.mainloop()
