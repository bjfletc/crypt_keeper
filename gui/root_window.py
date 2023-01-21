# going to be the launching point for the GUI part of the application

from tkinter import *
from gui.buttons import add_buttons


def build_root():
    root = Tk()
    root.title('Crypt Keeper 🗝️')
    root.geometry('400x400')
    add_buttons(root).pack()

    root.mainloop()
