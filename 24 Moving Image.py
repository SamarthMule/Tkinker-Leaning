from tkinter import *

def move_up(event):
    lable.place(x=lable.winfo_x(), y=lable.winfo_y() - 10)
def move_down(event):
    lable.place(x=lable.winfo_x(), y=lable.winfo_y() + 10)
def move_left(event):
    lable.place(x=lable.winfo_x() - 10, y=lable.winfo_y())
def move_right(event):
    lable.place(x=lable.winfo_x() + 10, y=lable.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

my_image = PhotoImage(file='Images/racecar.png')
lable = Label(window,image=my_image)
lable.place(x=0,y=0)

window.mainloop()