# holds the widgets associated with encrypting/decrypting files

from tkinter import *


def run_program_frame(parent_window, application_color):
    frame = Frame(parent_window, bg=application_color, width=300)
    frame.pack(side=LEFT, expand=False, fill=Y)

    # TODO: replace button text with image
    button = Button(frame, text='Encrypt File 🔒')
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    # used to force frame width, due to frame's setting width to their
    # children by default
    frame.pack_propagate(False)

