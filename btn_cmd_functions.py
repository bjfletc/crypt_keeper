# contains the functions for each button in the root application
# functions are ran when the buttons are pressed.
from tkinter import filedialog

file_path = ''


def choose_file():
    global file_path
    file_path = filepath = filedialog.askopenfilename()
