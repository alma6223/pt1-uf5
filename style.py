import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import scrolledtext

class Style:
    def root(geometry, title, icon):
        root = tk.Tk()
        root.geometry(geometry)
        root.title(title)
        root.iconbitmap(icon)
        root.resizable(False, False)
        return root

    def button(root, text, width, x, y, command):
        button = ttk.Button(root, text=text, width=width, command=command)
        button.place(x=x, y=y)
        return button

    def entry(root, width, x, y, insert):
        entry = ttk.Entry(root, width=width)
        entry.place(x=x, y=y)
        entry.insert(0, insert)
        return entry
    
    def combobox(root, procedures, width, x, y):
        combobox = ttk.Combobox(root, width=width, values=list(procedures.keys()))
        combobox.place(x=x, y=y)
        combobox.current(0)
        return combobox

    def label(root, text, x, y):
        label = ttk.Label(root, text=text)
        label.place(x=x, y=y)
        return label

    def image(root, file ,resize, x, y):
        global image
        image = ImageTk.PhotoImage(Image.open(file).resize(resize))
        label = ttk.Label(root, image=image)
        label.place(x=x, y=y)

    def scrolledtext(root, width, height, x, y):
        global scrolledtext
        scrolledtext = scrolledtext.ScrolledText(root, width=width, height=height)
        scrolledtext.place(x=x, y=y)
        return scrolledtext

    @classmethod
    def toplevel(cls, geometry, title, text, x, y):
        toplevel = tk.Toplevel()
        toplevel.geometry(geometry)
        toplevel.title(title)
        toplevel.resizable(False, False)
        cls.label(toplevel, text, x, y)



