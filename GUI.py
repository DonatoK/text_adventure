# This module will open a GUI screen.

import tkinter as tk


def launch_GUI():
    # Assume that this list gets updated automatically
    events = []

    # Make a Window oblect with some text in it.
    window_label = tk.Label(text="look at this window!")
    do_two = tk.Label(text="and this one is different",
                      foreground="white",  # Set the text color to white
                      background="black"  # Set the background color to black
                      )
    button = tk.Button(
        text="Click me!",
        width=25,
        height=5,
        bg="black",
        fg="yellow",
        )

    # "packs the objects and auto sizes text to fit in a window
    window_label.pack()
    do_two.pack()
    button.pack()
    # mainloop is required to keep the window open and for the gui to work from a
    # module
    window_label.mainloop()
    #do_two.mainloop()
    return
