# hold all aspects of entering the key, and choosing the application functionality
from tkinter import *


def enter_key_frame(parent_window, application_color):
    frame = Frame(parent_window, bg=application_color, width=300)
    frame.pack(side=LEFT, expand=False, fill=Y)

    button = Button(frame, text='Enter Key 🗝️')
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    # used to force frame width, due to frame's setting width to their
    # children by default
    frame.pack_propagate(False)
