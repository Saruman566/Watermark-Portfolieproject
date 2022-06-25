import tkinter
from tkinter import *
from PIL import ImageTk, Image, ImageGrab, ImageDraw, ImageFont
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

        try:
            for f in os.listdir('images'):
                self.images.append(f)
        except WindowsError:
            os.mkdir("images")

        if os.path.exists('./images/image0.png') is True:

            if self.images[2] == 'image10.png':
                self.images = natsorted(self.images, alg=ns.PATH | ns.IGNORECASE)

            self.pic = Image.open(f"images/{self.images[counter]}")
            self.img = ImageTk.PhotoImage(self.pic)
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
        self.pic = Image.open(f"images/{self.images[counter]}")
        self.img = ImageTk.PhotoImage(self.pic)
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
        self.pic = Image.open(f"images/{self.images[counter]}")
        self.img = ImageTk.PhotoImage(self.pic)
        self.w = self.img.width()
        self.h = self.img.height()
        self.img_label = Canvas(width=self.w, heigh=self.h, bg='#ffffff', bd=0, highlightthickness=0)
        self.pics = self.img_label.create_image(self.w / 2, self.h / 2, image=self.img)
        self.img_label.grid(column=0, row=0, sticky='NW')
        self.img_label.place(x=275, y=150)

    def water_m(self, intext, font, size, color):

        if font == "" or size == () or color == "":
            font = "arial.ttf"
            size = 10
            color = "white"

        self.img_label.delete('all')
        self.pic = Image.open(f"images/{self.images[counter]}")
        pic_with_text = ImageDraw.Draw(self.pic)
        te_font = ImageFont.truetype(font, int(size))
        pic_with_text.text((20, 15), intext, color, font=te_font)
        self.pic.save("images/img2.png")
        self.img_label.delete('all')
        self.pic = Image.open(f"images/img2.png")
        self.img = ImageTk.PhotoImage(self.pic)
        self.w = self.img.width()
        self.h = self.img.height()
        self.img_label = Canvas(width=self.w, heigh=self.h, bg='#ffffff', bd=0, highlightthickness=0)
        self.pics = self.img_label.create_image(self.w / 2, self.h / 2, image=self.img)
        self.img_label.grid(column=0, row=0, sticky='NW')
        self.img_label.place(x=275, y=150)


    def save_pics(self):

        self.save_pic = Image.open(f"images/img2.png")
        self.save_pic.save(filedialog.asksaveasfile(filetypes=[("jpg file", ".jpg")], defaultextension=".jpg"))
