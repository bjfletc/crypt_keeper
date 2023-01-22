from tkinter import *
from tkinter import filedialog

file_name = None


# TODO: look into adding icons for button images that are transparent

def choose_file():
    global file_name
    file_name = filedialog.askopenfilename()
    return file_name


def choose_file_button(frame):
    button = Button(frame, text='Choose file...', command=choose_file)
    # center choose_file button in the frame
    button.place(relx=0.5, rely=0.5, anchor=CENTER)
    return button
