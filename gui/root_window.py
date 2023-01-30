# launching point for the GUI part of the application

from gui.center_on_screen import center_window as center
from gui.section import *
from btn_cmd_functions import choose_file, enter_key_command, run
import gui.app_appearance as app


def build():
    root_window = Tk()
    root_window.title('Crypt Keeper 🔐')
    root_window.config(bg=app.COLOR)

    # center the root_window on screen
    center(root_window, app.WIDTH, app.HEIGHT)

    # create each section of the application's root window
    left_section = Section(root_window, app.COLOR, 'Choose File 📂', choose_file)
    middle_section = Section(root_window, app.COLOR, 'Cryptographic Key 🔑')
    right_section = Section(root_window, app.COLOR, 'Encrypt File 🔒', run)
    # change the name of the button after choosing a function with the middle button
    middle_section.button.config(command=lambda: enter_key_command(right_section))

    # display GUI
    root_window.mainloop()
