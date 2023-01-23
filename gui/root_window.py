# going to be the launching point for the GUI part of the application

from tkinter import *
from gui.choose_file_frame import choose_file_frame
from gui.cryptographic_key_frame import enter_key_frame
from gui.center_window import center_window
from gui.run_program_frame import run_program_frame

application_color = '#0A192F'


def build_root():
    root = Tk()
    root.title('Crypt Keeper 🔑️')
    root.config(bg=application_color)

    # center the root window, and set width 900, height 500
    center_window(root, 900, 500)

    choose_file_frame(root, application_color)

    # TODO: implement password button
    enter_key_frame(root, application_color)

    # TODO: implement running program function for button
    run_program_frame(root, application_color)

    root.mainloop()
