import turtle

ob = turtle.Turtle()
ob.speed(10)
cl=["red","green","blue"]

def draw(d,angle,x,y):
    c=0
    ob.up()
    ob.goto(x,y)
    ob.down()
    for i in range(1,100):
        ob.pencolor(cl[c])
        ob.forward(d)
        ob.left(angle)
        d= d-5
        c=c+1
        if(c>2):
            c=0
draw(200,98,0,0)