from tkinter import *
from gallery import Gallery
from watermark import *
import os


class Menubar(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)

        self.menu_canvas = tkinter.Canvas(width=1196, heigh=54, bg="#ffffff")
        self.menu_canvas.grid(column=0, row=0)
        self.menu_canvas.configure(bg="#ffffff", bd=0, highlightthickness=0)

        self.load_button = Button(text='Load Pictures', width=15, heigh=2,
                                  bg='#F24C4C', fg='#293462', command=self.get_pics)
        self.load_button.place(x=260, y=7)
        self.create_button = Button(text='Create Watermark', width=15, heigh=2, bg='#F24C4C', fg='#293462',
                                    command=self.watermark_creator)
        self.create_button.place(x=460, y=7)
        self.back_button = Button(text='Back', width=5, heigh=2, bg='#F24C4C', fg='#293462',
                                  command=self.back)
        self.back_button.place(x=650, y=7)
        self.next_button = Button(text='Next', width=5, heigh=2, bg='#F24C4C', fg='#293462',
                                  command=self.next)
        self.next_button.place(x=700, y=7)

        self.save_button = Button(text='Save pics', width=15, heigh=2, bg='#F24C4C', fg='#293462', command=self.save_pic)
        self.save_button.place(x=800, y=7)

        self.exit_button = Button(text='Exit', width=15, heigh=2, bg='#F24C4C', fg='#293462', command=self.go_out)
        self.exit_button.place(x=1055, y=7)

    def get_pics(self):

        file_names = filedialog.askopenfilenames()
        Menubar.make_thumbnails(self, file_names)

    def make_thumbnails(self, file_names):
        image = []
        thumbnail = []
        for pic in range(len(file_names)):
            image.append(file_names[pic])
            thumbnail.append(file_names[pic])
            image[pic] = Image.open(file_names[pic])
            thumbnail[pic] = Image.open(file_names[pic])
            image[pic].thumbnail((900, 900))
            image[pic].save(f'images/image{pic}.png')
            thumbnail[pic].thumbnail((200,200))
            try:
                thumbnail[pic].save(f'thumbnails/thumbnail{pic}.jpg')
            except FileNotFoundError:
                os.mkdir("thumbnails")
                thumbnail[pic].save(f'thumbnails/thumbnail{pic}.jpg')
            else:
                thumbnail[pic].save(f'thumbnails/thumbnail{pic}.jpg')

        if os.path.exists('./thumbnails') is True:

            Gallery.make_tpic(self=Gallery, file_names=file_names)
            worplace_container = tkinter.Frame(self)
            worplace_container.grid(column=1, row=1, sticky='NW')
            Workspace(self).__init__(parent=worplace_container)

    def go_out(self):

        try:
            for f in os.listdir("thumbnails"):
                os.remove(os.path.join("thumbnails", f))
        except WindowsError:
            pass
        try:
            for f in os.listdir("images"):
                os.remove(os.path.join("images", f))
        except WindowsError:
            pass
        exit()

    def next(self):

        Workspace(self).next_pic()

    def back(self):

        Workspace(self).back_pic()

    def watermark_creator(self):

        Watermark_interface()

    def save_pic(self):

        Workspace(self).save_pic()
