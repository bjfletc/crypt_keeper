# going to be the launching point for the GUI part of the application

from tkinter import *
from gui.buttons import choose_file_button

application_color = '#0A192F'


# TODO: build out the visual of the root window
def build_root():
    root = Tk()
    root.title('Crypt Keeper 🗝️')
    root.config(bg=application_color)

    # how to center window on screen solution found on
    # Stack Overflow: https://stackoverflow.com/a/14912644
    # start of Stack Overflow code...
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
    # end of Stack Overflow code...

    # frame to hold the choose_file button; set to 1/3rd of the
    # width of the window.
    left_frame = Frame(root, bg=application_color, width=300)
    left_frame.pack(side=LEFT, expand=False, fill=Y)

    # used to force frame width, due to frame's setting width to their
    # children by default
    left_frame.pack_propagate(0)

    choose_file_button(left_frame)

    root.mainloop()
