from tkinter import *


def submit():
    # print("You have ordered : ", end='')
    # print(listbox.get(listbox.curselection()))
    food = []
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    print("You Ordered : ")
    for f in food:
        print(f)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    # listbox.delete(listbox.curselection())
    for i in listbox.curselection():
        listbox.delete(i)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#F7FADE',
                  font=("Constantia", 35),
                  width=15,
                  selectmode=MULTIPLE,
                  borderwidth=10,
                  )
listbox.pack()
listbox.insert(1, "Pavbhaji")
listbox.insert(2, "Panipuri")
listbox.insert(3, "Vadapav")
listbox.insert(4, "Sangamvada")
listbox.insert(5, "Pakode")
listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()

deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()

window.mainloop()
