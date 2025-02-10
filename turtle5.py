import turtle

turtle.shape("turtle")
turtle.color("green")

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()

turtle.color("blue")
turtle.fillcolor("yellow")
turtle.begin_fill()
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

turtle.color("red")
turtle.fillcolor("orange")
turtle.begin_fill()
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

turtle.color("purple")
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()

turtle.done()