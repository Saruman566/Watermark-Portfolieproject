import tkinter.font
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from workspace import *
import os


class Watermark_interface(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)

        self.geometry("410x300")
        self.title("Watermark-Creator")
        self.configure(bg="#ffffff", bd=0, highlightthickness=0)

        self.Text_label = Label(self, text='Text', font='Cambria', width=10, height=3, bg='#ffffff', bd=0)
        self.Text_label.grid(column=0, row=0, sticky='NW')

        self.Text_field = Text(self, width=32, height=2, bg='#ffffff', font='MSSanSerif', padx=15, pady= 10)
        self.Text_field.grid(column=0, row=0, sticky='NW')
        self.Text_field.place(x=75)

        self.label = Label(self, text='Font', font='Cambria', width=10, height=3, bg='#ffffff', bd=0)
        self.label.grid(column=0, row=1, sticky='NW')

        self.fonts = [tkinter.font.families()[4], tkinter.font.families()[5], tkinter.font.families()[6],
        tkinter.font.families()[11],tkinter.font.families()[31],tkinter.font.families()[33]]

        self.font_box = ttk.Combobox(self,  values=self.fonts, width=40, state='readonly')
        self.font_box.grid(column=0, row=1, sticky='N')
        self.font_box.place(x=76, y=80)

        self.font_ok_button = Button(self, text='OK', width=3, heigh=1, command=self.others)
        self.font_ok_button.place(x=367, y=78)

        self.label = Label(self, text='Size', font='Cambria', width=10, height=3, bg='#ffffff', bd=0)
        self.label.grid(column=0, row=2, sticky='NW')

        size_list= [11,12,13,14,15,16,20]

        self.size_box = ttk.Combobox(self, values=size_list, width=40)
        self.size_box.grid(column=0, row=2, sticky='N')
        self.size_box.place(x=76, y=138)

        self.size_ok_button = Button(self, text='OK', width=3, heigh=1, command=self.others)
        self.size_ok_button.place(x=367, y=136)

        self.label = Label(self, text='Color', font='Cambria', width=10, height=3, bg='#ffffff', bd=0)
        self.label.grid(column=0, row=3, sticky='NW')

        a = "Blue"
        b = "Red"
        c = "Green"
        d = "Yellow"
        e = "White"
        f = "Black"

        colors = [a, b, c, d, e, f]

        self.color_box = ttk.Combobox(self, values=colors, width=40, state='readonly')
        self.color_box.grid(column=0, row=3, sticky='N')
        self.color_box.place(x=76, y=196)

        self.color_ok_button = Button(self, text='OK', width=3, heigh=1, command=self.others)
        self.color_ok_button.place(x=367, y=194)

        self.create_button = Button(self, text="Create", width=10, heigh=2, command=self.waterm_create)
        self.create_button.place(x=120, y=235)

        self.delete_button = Button(self, text="Delete", width=10, heigh=2, command=self.waterm_remove)
        self.delete_button.place(x=240, y=235)

    def waterm_create(self):

        input = self.Text_field.get("1.0", 'end-1c')
        font = self.font_box.get()
        size = self.size_box.get()
        color = self.color_box.get()

        if os.path.exists('./images/image0.jpg') is True:

            if font == "" or size == "" or color == "":
                font = 'Cambria'
                size = 10
                color = "#000000"
                input = self.Text_field.get("1.0", 'end-1c')
                Workspace(self).water_m(text=input, font=font, size=size, color=color)
            elif font == self.font_box.get() or input == self.Text_field.get("1.0", 'end-1c') or size == self.size_box.get():
                Workspace.water_m_remove(self=Workspace)
                input = self.Text_field.get("1.0", 'end-1c')
                font = self.font_box.get()
                size = self.size_box.get()
                Workspace(self).water_m(text=input, font=font, size=size, color=color)
            else:
                Workspace.water_m_remove(self=Workspace)
                input = self.Text_field.get("1.0", 'end-1c')
                font = self.font_box.get()
                size = self.size_box.get()
                Workspace(self).water_m(text=input, font=font, size=size, color=color)

    def waterm_remove(self):
        pass
        #Workspace.water_m_remove(self=Workspace)

    def others(self):

        Workspace.water_m_remove(self=Workspace)
        input = self.Text_field.get("1.0", 'end-1c')
        font = self.font_box.get()
        size = self.size_box.get()
        color = self.color_box.get()
        if color == "Blue":
            color = "#3B44F6"
        elif color == "Red":
            color = "#F32424"
        elif color == "Green":
            color = "#3EC70B"
        elif color == "Yellow":
            color = "#F7EC09"
        elif color == "White":
            color = "#ffffff"
        elif color == "Black":
            color = "#000000"

        if font == "":
            if size == "":
                if color == "":
                    font = 'Cambria'
                    size = 10
                    color = "#000000"
                    Workspace(self).water_m(text=input, font=font, size=size, color=color)
        elif size == "":
            size = 10
            color = "#000000"
            Workspace(self).water_m(text=input, font=font, size=size, color=color)
        elif color == "":
            color = "#000000"
            Workspace(self).water_m(text=input, font=font, size=size, color=color)
        else:
            Workspace.water_m_remove(self=Workspace)
            input = self.Text_field.get("1.0", 'end-1c')
            font = self.font_box.get()
            size = self.size_box.get()
            Workspace(self).water_m(text=input, font=font, size=size, color=color)
