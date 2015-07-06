import click
import multiprocessing as mp

from Tkinter import Frame, Tk, Button, LEFT, TOP
from threecolor.application import create_site
from threecolor.gunni import StandaloneApplication, number_of_workers, options

def startapp():
    StandaloneApplication(create_site(), options).run()
    return

p = mp.Process(target=startapp)

class Gooey:

    def __init__(self, master):

        mainframe = Frame(master)
        mainframe.pack()

        self.quitb = Button(
            mainframe, text="QUIT", fg="red", command=mainframe.quit
            )
        self.quitb.pack(side=LEFT)

        self.runb = Button(mainframe, text="Run 3color", command=self.runapp)
        self.runb.pack(side=TOP)

        self.launchb = Button(mainframe, text="Open in Browser", command=self.launchsite)
        self.launchb.pack(side=TOP)

        self.stopb = Button(mainframe, text="Stop 3color", command=self.stopapp)
        self.stopb.pack(side=TOP)

    def say_hi(self):
        print("Hellooooooo there")

    def runapp(self):
        """Run website locally in debug mode"""
        # app = create_site()
        # app.run(debug=False, port=5001)
        if p.is_alive():
            print("app not running")
        else:
            try:
                p.start()
            except:
                p.run()

    def launchsite(self):
        click.launch('http://localhost:5001/')

    def stopapp(self):
        if p.is_alive():
            p.terminate()
        else:
            print("app not running")


root = Tk()

gooey = Gooey(root)

root.mainloop()
