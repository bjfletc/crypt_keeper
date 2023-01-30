# launching point for the GUI part of the application

from gui.center_window_on_display import center_window
from gui.component import *
from btn_cmd_functions import choose_file, enter_key_command, run
import gui.app_appearance


def build_root():
    root = Tk()
    root.title('Crypt Keeper 🔐')
    root.config(bg=gui.app_appearance.COLOR)

    # center the root window, and set width 900, height 500
    center_window(root, 900, 500)

    left_component = Component(root, gui.app_appearance.COLOR, 'Choose File 📂', choose_file)
    middle_component = Component(root, gui.app_appearance.COLOR, 'Cryptographic Key 🔑')
    right_component = Component(root, gui.app_appearance.COLOR, 'Encrypt File 🔒', run)
    middle_component.button.config(command=lambda: enter_key_command(right_component))

    root.mainloop()
