from tkinter import *

window = Tk()

window.title("Labels in GUI program")
icon = PhotoImage(file='Images/apple-touch-icon.png')
window.iconphoto(True, icon)
photo = PhotoImage(file='Images/apple-touch-icon.png')
label = Label(window,
              text="Sam World",
              font=('Arial', 60, 'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label.pack()
# label.place(x=120,y=140)


window.mainloop()
