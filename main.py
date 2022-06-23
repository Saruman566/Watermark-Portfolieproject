import tkinter
from gallery import Gallery
from workspace import Workspace
from menubar import Menubar
from watermark import *


class Maininterface(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)

        self.title("Watermark-maker")
        self.configure(bg="#ffffff", bd=0, highlightthickness=0)

        menu_container = tkinter.Frame(self)
        menu_container.grid(column=0, row=0, sticky='N')

        gallery_container = tkinter.Frame(self)
        gallery_container.grid(column=0, row=1, sticky='NW')

        workplace_container = tkinter.Frame(self)
        workplace_container.grid(column=1, row=1, sticky='NW')

        first_frame = Menubar(parent=menu_container)
        first_frame.grid(column=0, row=0, sticky='NW')

        second_frame = Gallery(parent=gallery_container)
        second_frame.grid(column=0, row=0, sticky='NW')

        third_frame = Workspace(parent=workplace_container)
        third_frame.grid(column=0, row=0, sticky='NW')


if __name__ == "__main__":
    app = Maininterface()
    app.mainloop()
