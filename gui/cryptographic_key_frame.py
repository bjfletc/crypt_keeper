# hold all aspects of entering the key, and choosing the application functionality
from tkinter import *
from gui.center_window import center_window

cryptographic_key = ''
function = 0


# TODO: cleanup popup window code
def submit_function(key, func, window):
    global cryptographic_key
    global function
    cryptographic_key = key
    function = func.get()
    window.destroy()


def enter_key_command():
    # create a new window when someone presses the Enter Key button
    new_window = Toplevel()
    selection = IntVar()
    new_window.title('Choose Function & Enter Key 🔑')
    center_window(new_window, 900, 500)
    encryption_key_label = Label(new_window, text='Enter Cryptographic Key 🔑', padx=15)
    encryption_key_label.place(x=50, y=200)
    key_entry = Entry(new_window, width=40, show='*')
    key_entry.place(x=300, y=200)
    encrypt_radio_button = Radiobutton(new_window, text='Encrypt', variable=selection, value=0)
    decrypt_radio_button = Radiobutton(new_window, text='Decrypt', variable=selection, value=1)
    encrypt_radio_button.place(x=60, y=300)
    decrypt_radio_button.place(x=60, y=350)
    submit_button = Button(new_window, text='Submit', command=lambda: submit_function(key_entry.get(), selection
                                                                                      , new_window))
    submit_button.place(x=600, y=325)


def enter_key_frame(parent_window, application_color):
    frame = Frame(parent_window, bg=application_color, width=300)
    frame.pack(side=LEFT, expand=False, fill=Y)

    # TODO: replace button text with image
    button = Button(frame, text='Cryptographic Key 🔑️', command=enter_key_command)
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    # used to force frame width, due to frame's setting width to their
    # children by default
    frame.pack_propagate(False)
