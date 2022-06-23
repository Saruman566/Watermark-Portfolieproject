import tkinter
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import filedialog
import os
from natsort import natsorted, ns
counter = 0


class Workspace(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)

        self.main_frame = tkinter.Frame(self)
        self.main_frame.grid(column=1, row=1, sticky='NW')
        self.main_frame.place(x=252, y=56)
        self.main_canvas = Canvas(self.main_frame, width=944, heigh=844, bg="#ffffff")
        self.main_canvas.grid(column=1, row=1, sticky='NW')
        self.main_canvas.configure(bg="#ffffff", bd=0, highlightthickness=0)
        self.images = []

        for f in os.listdir('images'):
            self.images.append(f)

        if os.path.exists('./images/image0.jpg') is True:

            if self.images[2] == 'image10.jpg':
                self.images = natsorted(self.images, alg=ns.PATH | ns.IGNORECASE)

            self.img = ImageTk.PhotoImage(Image.open(f"images/{self.images[counter]}"))
            self.w = self.img.width()
            self.h = self.img.height()
            self.img_label = Canvas(width=self.w, heigh=self.h, bg='#ffffff', bd=0, highlightthickness=0)
            self.pics = self.img_label.create_image(self.w/2, self.h/2, image=self.img)
            self.img_label.grid(column=0, row=0, sticky='NW')
            self.img_label.place(x=275, y=150)

    def next_pic(self):

        global counter

        if self.images[counter] == self.images[-1]:
            counter = -1
        else:
            counter += 1

        self.img_label.delete('all')
        self.img = ImageTk.PhotoImage(Image.open(f"images/{self.images[counter]}"))
        self.w = self.img.width()
        self.h = self.img.height()
        self.img_label = Canvas(width=self.w, heigh=self.h, bg='#ffffff', bd=0, highlightthickness=0)
        self.pics = self.img_label.create_image(self.w / 2, self.h / 2, image=self.img)
        self.img_label.grid(column=0, row=0, sticky='NW')
        self.img_label.place(x=275, y=150)

    def back_pic(self):

        global counter

        if self.images[counter] == self.images[0]:
            counter = 0
        else:
            counter -= 1

        self.img_label.delete('all')
        self.img = ImageTk.PhotoImage(Image.open(f"images/{self.images[counter]}"))
        self.w = self.img.width()
        self.h = self.img.height()
        self.img_label = Canvas(width=self.w, heigh=self.h, bg='#ffffff', bd=0, highlightthickness=0)
        self.pics = self.img_label.create_image(self.w / 2, self.h / 2, image=self.img)
        self.img_label.grid(column=0, row=0, sticky='NW')
        self.img_label.place(x=275, y=150)

    def water_m(self, text, font, size, color):

        self.waterm_field = ImageDraw.Draw(self.img_label)
        self.waterm_field.text(90,15, text=text, font=(font, size), fill=color)

    def water_m_remove(self):
        pass
        #self.waterm_field.destroy()

    def save_pics(self):
        #x = self.winfo_rootx()+self.winfo_x()
        #y = self.winfo_rooty()+self.winfo_y()
        #x1=x+Workspace(self).img_label.winfo_width()
        #y1=y+Workspace(self).img_label.winfo_height()
        #ImageGrab.grab().crop((x,y,x1,y1))
        self.img.save(filedialog.asksaveasfile(filetypes=[("jpg file", ".jpg")], defaultextension=".jpg"))