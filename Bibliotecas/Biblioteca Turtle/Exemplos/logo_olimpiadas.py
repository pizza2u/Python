#Importing Turtle
import turtle
#set the pensize to 8
turtle.pensize(8)

#first ring
turtle.color('blue')
turtle.penup()
#set the x and y coordinates to -110 and -25
turtle.goto(-110,-25)
turtle.pendown()
#set radius of circle to 50
turtle.circle(50)

#second ring
turtle.color('black')
turtle.penup()
turtle.goto(0,-25)
turtle.pendown()
turtle.circle(50)

#Third ring
turtle.color('red')
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(50)

#fourth ring
turtle.color('yellow')
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(50)


#fifth ring
turtle.color('green')
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(50)
turtle.done()