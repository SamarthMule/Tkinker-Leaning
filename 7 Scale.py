from tkinter import *


def submit():
    print("The temperature is : "+ str(scale.get()) + " degrees C")


window = Tk()

hotImage = PhotoImage(file='Images/Hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,    # orientation of scale
              font=("Consolas", 20),
              tickinterval=10,  # adds numeric indicator
              # showvalue=False,   # hide current value
              resolution=5,  # increment of slider
              troughcolor='blue',
              fg='#FF1C00',
              bg='#111111'
              )
scale.set(50)
scale.pack()
coldImage = PhotoImage(file='Images/Cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()
button = Button(window,
                text="Submit",
                command=submit)
button.pack()

window.mainloop()
