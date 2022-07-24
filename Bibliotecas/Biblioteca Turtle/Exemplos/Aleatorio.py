import turtle
# Aleatório
ninja = turtle.Turtle()
ninja.color("white", "red")
ninja.pensize(1)
turtle.bgcolor("black")
ninja.speed(100)

for i in range(180):
    ninja.forward(100)
    ninja.right(200)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(20, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()