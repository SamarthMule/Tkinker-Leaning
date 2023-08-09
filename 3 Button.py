from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)


window = Tk()

photo = PhotoImage(file='Images/click.png')
window.title("Buttons in GUI program")
icon = PhotoImage(file='Images/apple-touch-icon.png')
window.iconphoto(True, icon)
button = Button(window,
                text='click',
                command=click,
                font=('Comic Sans', 30),
                fg="black",
                bg="green",
                activebackground="#00FF00",
                activeforeground="black",
                state=ACTIVE,
                image=photo,
                compound='left')  # DISABLED
button.pack()

window.mainloop()
