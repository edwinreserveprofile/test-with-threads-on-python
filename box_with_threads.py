import turtle, random

from threading import *

window = turtle.Screen()

border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('black')
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)

count_balls = 2

class Ball:

    dx, dy = random.randint(8,16), random.randint(4,8)

    def __init__(self):
        self.obj = turtle.Turtle()
        self.obj.hideturtle()
        self.obj.shape('circle')
        self.obj.up()
        self.obj.goto(random.randint(-300, 300), random.randint(-300, 300))
        self.obj.color('lime')
        self.obj.showturtle()

    def move(self):
        x, y = self.obj.position()
        if abs(x+self.dx)>=300:
            self.dx = -1*self.dx
        if abs(y+self.dy)>=300:
            self.dy = -1*self.dy
        self.obj.goto(x+self.dx , y+self.dy)

def entropia(self):
    while True:
        self.move()

for i in range(count_balls):
    Thread(target=entropia,args=(Ball(),)).start()

window.mainloop()