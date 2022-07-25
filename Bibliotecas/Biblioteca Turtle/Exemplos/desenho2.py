import turtle

colors = ['red','yellow','green','pink','blue','purple']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(10)

for i in range(500):
    t.pencolor(colors[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(59)
