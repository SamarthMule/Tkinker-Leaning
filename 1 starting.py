from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Sam's First GUI program")
icon = PhotoImage(file='Images/apple-touch-icon.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")
window.mainloop()