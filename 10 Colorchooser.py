from tkinter import *
from tkinter import colorchooser  # submodule


def click():
    # color = colorchooser.askcolor()
    # # print(color)
    # colorhex = color[1]
    # # print(colorhex)
    # window.config(bg=str(colorhex))  # change background color
    # noinspection PyTypeChecker
    window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("480x480")

button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()
