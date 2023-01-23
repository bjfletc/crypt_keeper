# hold all aspects of entering the key, and choosing the application functionality
from tkinter import *
from gui.center_window import center_window


def enter_key_command():
    # create a new window when someone presses the Enter Key button
    new_window = Toplevel()
    new_window.title('Choose Function & Enter Key 🗝️')
    center_window(new_window, 900, 500)


def enter_key_frame(parent_window, application_color):
    frame = Frame(parent_window, bg=application_color, width=300)
    frame.pack(side=LEFT, expand=False, fill=Y)

    # TODO: replace button text with image
    button = Button(frame, text='Cryptographic Key 🔑️', command=enter_key_command)
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    # used to force frame width, due to frame's setting width to their
    # children by default
    frame.pack_propagate(False)
