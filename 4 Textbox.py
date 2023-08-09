from tkinter import *


def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg="#00F000",
              bg="black")
# entry.insert(0,"Samarth Mule")
# entry.config(state=DISABLED)
# entry.config(show="*") for password
entry.pack(side=LEFT)

submit_but = Button(window, text="Submit", command=submit)
submit_but.pack(side=RIGHT)

delete_but = Button(window, text="Delete", command=delete)
delete_but.pack(side=RIGHT)

backspace_but = Button(window, text="Backspace", command=backspace)
backspace_but.pack(side=RIGHT)

window.mainloop()
