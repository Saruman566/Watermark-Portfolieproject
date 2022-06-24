import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os

class Gallery(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)

        canvas = Canvas(width=250, heigh=842, bg="#ffffff")
        canvas.grid(column=0, row=1, sticky='Nw')
        canvas.configure(bg="#ffffff", bd=0, highlightthickness=0)

    def make_tpic(self, file_names):

        canvas = Canvas(width=250, heigh=842, bg='#ffffff', scrollregion=(0, 0, 0, (len(file_names)*105)))
        hbar = Scrollbar(canvas, command=canvas.yview)
        hbar.place(x=235, y=0, height=844)
        hbar.config(command=canvas.yview)
        canvas.config(yscrollcommand=hbar.set)
        canvas.grid(column=0, row=1, sticky='Nw')

        t = 0
        z = 75

        for pic in range((len(file_names))):
            img = ImageTk.PhotoImage(Image.open(f'thumbnails/thumbnail{t}.jpg'))
            label = Label(image=img)
            label.image = img
            canvas.create_window(120, z, window=label)
            z += 100
            t += 1