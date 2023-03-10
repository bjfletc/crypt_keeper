# author: Brandon Fletcher
# e-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc
# crypt_keeper 🔐:  an application to be used on macOS/Linux for the purpose of
#                   encrypting/decrypting files using AES-256-CBC encryption that is built into
#                   the operating system of these platforms.

from gui.root_window import build


def main():
    # launches the root window of the program
    build()
    # ⬆️ application will hang here until GUI is closed. may need
    # to look into threading if I need it to do other things at this point after the
    # window is opened, while the program is running.


if __name__ == '__main__':
    main()
