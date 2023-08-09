from tkinter import *

def doSomething(event):
    # print("You did a thing !")
    # print("You pressed : " + event.keysym)
    lable.config(text=event.keysym)

window = Tk()

window.bind("<Key>", doSomething)
lable = Label(window,font=("Helvetica",100))
lable.pack()

window.mainloop()
