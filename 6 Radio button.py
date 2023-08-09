from tkinter import *

food = ["PavBhaji", "Vadapav", "Panipuri"]


def order():
    if x.get() == 0:
        print(f"Ordered Food is {food[0]}")
    elif x.get() == 1:
        print(f"Ordered Food is {food[1]}")
    elif x.get() == 2:
        print(f"Ordered Food is {food[2]}")
    else:
        print("Ordered ?")


window = Tk()

PavBhajiImage = PhotoImage(file='Images/PavBhaji.png')
VadapavImage = PhotoImage(file='Images/Vadapav.png')
PanipuriImage = PhotoImage(file='Images/Panipuri.png')
FoodImages = [PavBhajiImage, VadapavImage, PanipuriImage]

x = IntVar()
for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],  # adds text
                               variable=x,  # groups radiobutton
                               value=index,  # assigns each radiobutton a different value
                               padx=25,
                               font=("Impact", 45),
                               image=FoodImages[index],
                               compound=RIGHT,
                               indicatoron=False,   # eliminate circle indicator
                               width=450,   # set width
                               command=order    # set command to radiobutton to function
                               )
    radio_button.pack(anchor=W)

window.mainloop()
