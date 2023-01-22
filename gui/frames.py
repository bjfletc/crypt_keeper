from tkinter import *


def left_frame(window, application_color):
    frame = Frame(window, bg=application_color, width=300)
    frame.pack(side=LEFT, expand=False, fill=Y)

    # used to force frame width, due to frame's setting width to their
    # children by default
    frame.pack_propagate(False)
    return frame
