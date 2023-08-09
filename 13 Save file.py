from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="D:\\Python Programs\\TkinkerProject",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text File", ".txt"),
                                        ("HTML File", ".html"),
                                        ("All File", ".*")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    # filetext = input("Enter Any Input : ")
    file.write(filetext)
    file.close()


window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 25),
            height=8, width=20,
            pady=20, padx=20,
            foreground="purple"
            )
text.pack()
button = Button(text="Save", command=saveFile)
button.pack()

window.mainloop()
