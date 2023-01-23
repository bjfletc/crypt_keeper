# hold all aspects of choosing the file to encrypt/decrypt for the application
from tkinter import *
from tkinter import filedialog

filepath = ''


def choose_filepath():
    global filepath
    filepath = filedialog.askopenfilename()


def choose_file_frame(parent_window, application_color):
    frame = Frame(parent_window, bg=application_color, width=300)
    frame.pack(side=LEFT, expand=False, fill=Y)

    button = Button(frame, text='Select File 📂', command=choose_filepath)
    # center choose_file button in the frame
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    # used to force frame width, due to frame's setting width to their
    # children by default
    frame.pack_propagate(False)

