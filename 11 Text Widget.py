from tkinter import *


def submit():
    inputs = text.get("1.0", END)
    print(inputs)


window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink Free", 25),
            height=8, width=20,
            pady=20,padx=20,
            foreground="purple"
            )
text.pack()
button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
