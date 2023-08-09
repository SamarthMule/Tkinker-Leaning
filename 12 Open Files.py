from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Python Programs\\TkinkerProject",
                                          title="Open File",
                                          filetypes=(("text files", "*.txt"), ("All file", "*.*"))
                                          )
    # print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open", command=openfile)
button.pack()

window.mainloop()