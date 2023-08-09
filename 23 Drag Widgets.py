from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    xx = widget.winfo_x() - widget.startX + event.x
    yy = widget.winfo_y() - widget.startY + event.y
    widget.place(x=xx,y=yy)

window = Tk()

lable = Label(window,bg='red',width=10,height=5)
lable.place(x=0,y=0)

lable2 = Label(window,bg='blue',width=10,height=5)
lable2.place(x=110,y=110)

lable.bind("<Button-1>",drag_start)
lable.bind("<B1-Motion>",drag_motion)

lable2.bind("<Button-1>",drag_start)
lable2.bind("<B1-Motion>",drag_motion)

window.mainloop()