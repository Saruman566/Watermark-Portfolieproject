import tkinter.font
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from workspace import *
import os


class Watermark_interface(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)

        self.geometry("380x350")
        self.title("Watermark-Creator")
        self.configure(bg="#ffffff", bd=0, highlightthickness=0)

        self.Text_label = Label(self, text='Text', font='Cambria', width=10, height=3, bg='#ffffff', bd=0)
        self.Text_label.grid(column=0, row=0, sticky='NW')
        self.Text_label.place(y=25)

        self.Text_field = Text(self, width=26, height=2, bg='#ffffff', font='MSSanSerif', padx=15, pady= 10)
        self.Text_field.grid(column=0, row=0, sticky='NW')
        self.Text_field.place(x=75, y=25)

        self.font_label = Label(self, text='Font', font='Cambria', width=10, height=3, bg='#ffffff', bd=0)
        self.font_label.grid(column=0, row=1, sticky='NW')
        self.font_label.place(y=85)

        self.fonts = [tkinter.font.families()[11],tkinter.font.families()[31],tkinter.font.families()[33]]

        self.font_box = ttk.Combobox(self,  values=self.fonts, width=40, state='readonly')
        self.font_box.grid(column=0, row=1, sticky='N')
        self.font_box.place(x=76, y=105)

        self.size_label = Label(self, text='Size', font='Cambria', width=10, height=3, bg='#ffffff', bd=0)
        self.size_label.grid(column=0, row=2, sticky='NW')
        self.size_label.place(y=143)

        size_list= [11,12,13,14,15,16,20]

        self.size_box = ttk.Combobox(self, values=size_list, width=40)
        self.size_box.grid(column=0, row=2, sticky='N')
        self.size_box.place(x=76, y=163)

        self.color_label = Label(self, text='Color', font='Cambria', width=10, height=3, bg='#ffffff', bd=0)
        self.color_label.grid(column=0, row=3, sticky='NW')
        self.color_label.place(y=200)

        a = "blue"
        b = "red"
        c = "green"
        d = "yellow"
        e = "white"
        f = "black"

        colors = [a, b, c, d, e, f]

        self.color_box = ttk.Combobox(self, values=colors, width=40, state='readonly')
        self.color_box.grid(column=0, row=3, sticky='N')
        self.color_box.place(x=76, y=220)

        self.create_button = Button(self, text="Create", width=10, heigh=2, command=self.text_create)
        self.create_button.place(x=160, y=265)

    def text_create(self, *args):

        if os.path.exists('./images/image0.png') is True:

            intext = self.Text_field.get("1.0", 'end-1c')
            font = self.font_switch()
            size = self.size_switch()
            color = self.color_switch()
            Workspace(self).water_m(intext, font, size, color)

    def font_switch(self):

        font = self.font_box.get()

        if font == tkinter.font.families()[11]:
            font = "arial.ttf"
        elif font == tkinter.font.families()[31]:
            font = "calibri.ttf"
        elif font == tkinter.font.families()[33]:
            font = "cambriab.ttf"

        return font

    def size_switch(self):

        size = self.size_box.get()

        if size == "":
            size = 10

        return size

    def color_switch(self):

        color = self.color_box.get()

        if color == "":
            color = 'white'

        return color
