from tkinter import *

def create_window():
    # new_window = Toplevel()   # Toplevel() = new window 'on top' of other window, linked to a 'bottom' window
    new_window = Tk()           # new independent window
    Old_window.destroy()        # close out of old window

Old_window = Tk()

button = Button(Old_window, text="Create New Window", command=create_window)
button.pack()

Old_window.mainloop()