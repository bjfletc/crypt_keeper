# used to center a window on the screen

# how to center window on screen solution found on
# Stack Overflow: https://stackoverflow.com/a/14912644


def center_window(window, width, height):
    w = width
    h = height

    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
