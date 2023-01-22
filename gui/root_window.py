# going to be the launching point for the GUI part of the application

from tkinter import *
from gui.buttons import add_buttons


# TODO: build out the visual of the root window
def build_root():
    root = Tk()
    root.title('Crypt Keeper 🗝️')
    root.config(bg='#0a192f')
    add_buttons(root).pack()

    # how to center window on screen solution found on
    # Stack Overflow: https://stackoverflow.com/a/14912644
    w = 900  # width for the Tk root
    h = 500  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.mainloop()
