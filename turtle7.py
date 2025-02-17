import turtle

radius = int(input("Enter the radius of the circle: "))

t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(-50, -50 - radius)
t.pendown()

t.color("blue", "yellow")

t.begin_fill()
t.circle(radius)
t.end_fill()

t.hideturtle()

turtle.done()
