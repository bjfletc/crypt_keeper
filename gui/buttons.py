from tkinter import *


# TODO: look into adding icons for button images that are transparent

def choose_file_button(frame):
    button = Button(frame, text='Choose file...')
    # center choose_file button in the frame
    button.place(relx=0.5, rely=0.5, anchor=CENTER)
    return button
