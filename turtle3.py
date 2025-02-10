import turtle

t = turtle.Turtle()

turtle.bgcolor("black")
t.color("red", "pink")

t.begin_fill()
for _ in range(36):
    t.circle(100, steps=3)
    t.left(10)
t.end_fill()

t.hideturtle()

turtle.done()