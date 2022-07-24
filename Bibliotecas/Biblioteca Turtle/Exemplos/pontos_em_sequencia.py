from turtle import Screen, Turtle
stepsize = 10

def draw_triangles(tur, dot, steps=1):
    a, b = turtle.position()

    for step in range(steps):
        turtle.goto(a, b + step * stepsize)
        turtle.dot()

        for _ in range(steps - step - 1):
            turtle.backward(stepsize)
            turtle.dot()

    if steps < dot:
        turtle.goto(a + stepsize * (steps + 2), b)
        draw_triangles(turtle, dot, steps + 1)

screen = Screen()

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

draw_triangles(turtle, 6)

screen.exitonclick()
