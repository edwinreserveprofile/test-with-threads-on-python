import turtle, random
window = turtle.Screen()
border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('black')
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)
n = 7
dx = [random.randint(8,16) for i in range(n)]
dy = [random.randint(4,8) for i in range(n)]
def g(obj,i):
    global dx , dy
    x,y = obj.position()
    if abs(x + dx[i]) >= 300:
        dx[i] = -1*dx[i]
    if abs(y + dy[i]) >= 300:
        dy[i] = -1*dy[i]
    obj.goto(x+dx[i],y+dy[i])
balls = [turtle.Turtle() for i in range(n)]
for i in balls:
    i.hideturtle()
    i.shape('circle')
    i.up()
    i.goto(random.randint(-250,250),random.randint(-250,250))
    i.color('gold')
    i.showturtle()
cur = 0
while True:
    for i in balls:
        g(i,cur)
        if cur == n-1:
            cur = 0
        else:
            cur += 1
window.mainloop()