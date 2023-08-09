from tkinter import *
import time

xVelocity = 5
yVelocity = 3
window = Tk()
backgroungimage = PhotoImage(file="Images/background.png")
WIDTH = backgroungimage.width()
HEIGHT = backgroungimage.height()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

my = canvas.create_image(0,0,image=backgroungimage,anchor=NW)

photoimage = PhotoImage(file="Images/stop (2).png")
my_image = canvas.create_image(0,0,image=photoimage,anchor=NW)

image_width = photoimage.width()
image_height = photoimage.height()

while True:
    coordinate = canvas.coords(my_image)
    # print(coordinate)
    if(coordinate[0] >= WIDTH - image_width or coordinate[0] < 0):
        xVelocity = -xVelocity
    if (coordinate[1] >= HEIGHT - image_height or coordinate[1] < 0):
        yVelocity = -yVelocity

    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
