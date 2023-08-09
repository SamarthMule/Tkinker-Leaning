from tkinter import *

window = Tk()
window.config(height=400, width=400)
frame = Frame(window,
              bg="pink", bd=5,
              relief=SUNKEN)
# frame.pack(side=BOTTOM)
frame.place(x=100, y=100)
# button = Button(window, text="W", font=("Consolas",25), width=3)
# button.pack()
Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

window.mainloop()
