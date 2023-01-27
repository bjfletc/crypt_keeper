# launching point for the GUI part of the application

from gui.center_window import center_window
from gui.component import *

application_color = '#0A192F'


def build_root():
    root = Tk()
    root.title('Crypt Keeper 🔐')
    root.config(bg=application_color)

    # center the root window, and set width 900, height 500
    center_window(root, 900, 500)

    left_component = Component(root, application_color, 'Choose File 📂')
    middle_component = Component(root, application_color, 'Cryptographic Key 🔑')
    right_component = Component(root, application_color, 'Encrypt File 🔒')

    root.mainloop()
