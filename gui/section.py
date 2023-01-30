# a Component is the culmination of a Frame, and Button. Needed for the root window
# of the application where there are three buttons, each contained in its own frame.

from tkinter import *


class Section:

    def __init__(self, parent_window, app_color, button_name=None, button_command=None):

        self.parent_window = parent_window
        self.app_color = app_color
        self.button_name = button_name
        self.button_command = button_command

        # create a frame, and attach it to the parent window from the constructor
        self.frame = Frame(self.parent_window, bg=self.app_color, width=300)
        self.frame.pack(side=LEFT, expand=False, fill=Y)

        # add the button to the frame
        self.button = Button(self.frame, text=self.button_name, command=self.button_command)
        # center button in frame
        self.button.place(relx=0.5, rely=0.5, anchor=CENTER)

        # force frame width, due to frame's width being set to the child's width
        # by default
        self.frame.pack_propagate(False)
