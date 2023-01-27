# contains the functions for each button in the root application
# functions are ran when the buttons are pressed.
from tkinter import filedialog
from tkinter import *
from gui.center_window_on_display import center_window
from os import system
from cryptographic_functions import encrypt_file, decrypt_file

file_path = ''
cryptographic_key = ''
function = 0


# section that contains the left button logic
def choose_file():
    global file_path
    file_path = filepath = filedialog.askopenfilename()


# section that houses the middle button logic
# TODO: cleanup popup window code
def submit_function(key, func, window, component):
    global cryptographic_key
    global function
    cryptographic_key = key
    function = func.get()
    if function == 0:
        component.button.config(text='Encrypt File 🔒')
    else:
        component.button.config(text='Decrypt File 🔓')
    window.destroy()


def enter_key_command(component):
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
                                                                                      , new_window, component))
    submit_button.place(x=600, y=325)


# right component functionality

def run():
    if function == 0:
        print(encrypt_file(file_path, cryptographic_key))
        system(encrypt_file(file_path, cryptographic_key))
    elif function == 1:
        print(decrypt_file(file_path, cryptographic_key))
        system(decrypt_file(file_path, cryptographic_key))
    else:
        print('Do nothing.')
