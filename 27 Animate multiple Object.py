class Ball:
    def __int__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,fill=color)
        self.xV = xVelocity
        self.yV = yVelocity
    def move(self):
        coodinates = self.canvas.coords(self.image)
        print(coodinates)
        self.canvas.move(self.image,self.xV,self.yV)
        if (coodinates[2] >= (self.canvas.winfo_width()) or coodinates[0] < 0):
            self.xV = -self.xV
        if (coodinates[3] >= (self.canvas.winfo_height()) or coodinates[1] < 0):
            self.yV = -self.yV


from tkinter import *
import time

window = Tk()
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

# volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,100,2,3,"blue")

while True:
    # volley_ball.move()
    tennis_ball.move()
    window.update()
    time(0.01)

window.mainloop()
