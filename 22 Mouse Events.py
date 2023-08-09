from tkinter import *


def doSomething(event):
    # print("You did a thing !")
    print("Mouse Coordinates : " + str(event.x) + "," + str(event.y))


window = Tk()

# window.bind("<Button-1>", doSomething)  # left mouse click
# window.bind("<Button-2>", doSomething)  # scroll wheel
# window.bind("<Button-3>", doSomething)  # right mouse click
# window.bind("<ButtonRelease>", doSomething)
# window.bind("<Enter>", doSomething)     # enter the window
# window.bind("<Leave>",doSomething)      # leave the window
window.bind("<Motion>", doSomething)  # where the mouse moved

window.mainloop()
