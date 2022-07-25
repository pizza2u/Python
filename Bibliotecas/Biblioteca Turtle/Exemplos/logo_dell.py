import turtle

t=turtle.Turtle()

t.pensize(15)
t.color("#3287c1","#3287c1")
t.penup()
t.goto(20,-200)
t.pendown()
t.circle(180)
t.penup()


#Draw the "D" of the DELL logo
t.pensize(2)
t.goto(-130,-70)
t.pendown()
t.setheading(90)
t.forward(90)
t.right(90)
t.forward(50)
t.penup()
t.goto(-130,-70)
t.setheading(0)
t.pendown()
t.forward(50)
t.left(10)
t.circle(46,165)
t.penup()

t.color("#3287c1")
t.goto(-130,-70)
t.setheading(0)
t.pendown()
t.begin_fill()

t.forward(20)
t.left(90)
t.forward(90)
t.left(90)
t.forward(20)
t.end_fill()
t.backward(20)
t.left(90)
t.forward(17)
t.setheading(0)
t.begin_fill()
t.forward(30)
t.right(25)
t.circle(-30,130)
t.setheading(180)
t.forward(30)
t.left(90)
t.forward(17)
t.setheading(0)
t.forward(30)
t.left(10)
t.circle(45,165)
t.setheading(180)
t.forward(47)
t.end_fill()
t.penup()

#Draw the 'E' of the DELL logo
t.goto(-45,-15)
t.pendown()
t.setheading(0)
t.left(35)
t.begin_fill()
t.forward(65)
t.right(90)
t.forward(18)
t.right(90)
t.forward(50)
t.left(90)
t.forward(10)
t.left(90)
t.forward(50)
t.right(90)
t.forward(18)
t.right(90)
t.forward(50)
t.left(90)
t.forward(10)
t.left(90)
t.forward(50)
t.right(90)
t.forward(18)
t.right(90)
t.forward(65)
t.right(85)
t.forward(65)
t.penup()
t.end_fill()

#Draw the 'L' of the DELL logo
t.goto(40,-70)
t.setheading(90)
t.pendown()
t.begin_fill()
t.forward(90)
t.right(90)
t.forward(20)
t.right(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.end_fill()
t.penup()

#Draw the 'l' of the DELL Logo
t.goto(110,-70)
t.setheading(90)
t.pendown()
t.begin_fill()
t.forward(90)
t.right(90)
t.forward(20)
t.right(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.end_fill()
t.penup()
t.hideturtle()

turtle.done()