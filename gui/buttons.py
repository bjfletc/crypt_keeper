from tkinter import *
from tkinter import filedialog

file_name = ''


# TODO: look into adding icons for button images that are transparent

def choose_file():
    global file_name
    file_name = filedialog.askopenfilename()
    return file_name


def key_function_window():
    new_window = Toplevel()
    new_window.title('Choose Function & Enter Key 🗝️')
    w = 900  # width for the Tk root
    h = 500  # height for the Tk root

    # get screen width and height
    ws = new_window.winfo_screenwidth()  # width of the screen
    hs = new_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk new_window window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    new_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return new_window


def choose_file_button(frame):
    button = Button(frame, text='Choose file...', command=choose_file)
    # center choose_file button in the frame
    button.place(relx=0.5, rely=0.5, anchor=CENTER)
    return button


# TODO: implement password button function
def enter_key_button(frame):
    button = Button(frame, text='Enter Key 🗝️', command=key_function_window)
    button.place(relx=0.5, rely=0.5, anchor=CENTER)
    return button
