from tkinter import *
from tkinter import filedialog
import shutil

def copyfile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Python Programs",
                                          title="Open File",
                                          filetypes=((("All file", "*.*")))
                                          )
    shutil.copy(filepath,"D:\\Python Programs\\TkinkerProject\\")

def movefile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Python Programs",
                                          title="Open File",
                                          filetypes=(("All file", "*.*"))
                                          )
    shutil.move(filepath,"D:\\Python Programs\\TkinkerProject\\")

window = Tk()

button = Button(text="Copy", command=copyfile)
button.pack()
button2 = Button(text="Move", command=movefile)
button2.pack()

window.mainloop()