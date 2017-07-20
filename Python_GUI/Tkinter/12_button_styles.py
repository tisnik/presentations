#!/usr/bin/env python

from tkinter import *

import sys

root = Tk()

button1 = Button(root, background='yellow', text="1st btn",
                 command=lambda: sys.exit(0))
button2 = Button(root, background='#ff8080', text="Second button",
                 command=lambda: sys.exit(0))
button3 = Button(root, text="Third button",
                 command=lambda: sys.exit(0))
button4 = Button(root, text="This is fourth button, the last one",
                 command=lambda: sys.exit(0))

button3.configure(background='#8080ff')
button4['background'] = '#80ff80'

button1.grid(column=1, row=1, sticky="we")
button2.grid(column=2, row=1, sticky="we")
button3.grid(column=1, row=2, sticky="we")
button4.grid(column=2, row=2, sticky="we")

root.mainloop()
