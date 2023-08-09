from tkinter import *

def display():
    # if x.get() == 1:
    #     print("Work is Done")
    # else:
    #     print("Work is not done")
    # if x.get() == True:
    #     print("Work is Done")
    # else:
    #     print("Work is not done")
    if x.get() == "Yes":
        print("Work is Done")
    else:
        print("Work is not done")


window = Tk()

photo = PhotoImage(file="Images/Done.png")
# x = IntVar()
# x = BooleanVar
x = StringVar()
check_button = Checkbutton(window,
                           text="This Work Is Done",
                           variable=x,
                           # onvalue = 1
                           # offvalue = 0
                           # onvalue=True,
                           # offvalue=False,
                           onvalue="Yes",
                           offvalue="No",
                           command=display,
                           font=('Arial', 50),
                           fg='#0000FF',
                           bg='black',
                           # activeforeground='#FF0000',
                           # activebackground='#00FF00',
                           activeforeground='#0000FF',
                           activebackground='black',
                           pady=20,
                           padx=10,
                           image=photo,
                           compound=LEFT)
check_button.pack()

window.mainloop()
