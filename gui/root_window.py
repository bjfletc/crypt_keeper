# launching point for the GUI part of the application

from gui.center_window_on_display import center_window
from gui.component import *
from btn_cmd_functions import choose_file, enter_key_command

application_color = '#0A192F'


def build_root():
    root = Tk()
    root.title('Crypt Keeper 🔐')
    root.config(bg=application_color)

    # center the root window, and set width 900, height 500
    center_window(root, 900, 500)

    left_component = Component(root, application_color, 'Choose File 📂', choose_file)
    middle_component = Component(root, application_color, 'Cryptographic Key 🔑', enter_key_command)
    right_component = Component(root, application_color, 'Encrypt File 🔒')

    root.mainloop()
