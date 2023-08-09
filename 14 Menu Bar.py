from tkinter import *


def openFile():
    print("File is Opened")


def saveFile():
    print("File is Saved")


def cut():
    print("You Cut Some Text")


def copy():
    print("You Copy Some Text")


def paste():
    print("You Paste Some Text")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

openImage = PhotoImage(file="Images/folder.png")
saveImage = PhotoImage(file="Images/diskette.png")
exitImage = PhotoImage(file="Images/stop (1).png")
FileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="Open", command=openFile, image=openImage, compound=LEFT)
FileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound=LEFT)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quit, image=exitImage, compound=LEFT)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()
