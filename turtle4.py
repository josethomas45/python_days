import turtle
import random

t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("midnight blue")


t.penup()
t.goto(-200, 100)
t.pendown()
t.color("light yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

t.color("white")
for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(10)
        t.right(144)
    t.end_fill()

def draw_cloud(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(6):
        t.circle(20, 180)
        t.right(120)
    t.end_fill()

draw_cloud(100, 200)
draw_cloud(200, 150)
draw_cloud(-100, 250)

t.speed(10)

def draw_bird(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.setheading(45)
    t.circle(10, 90)
    t.setheading(135)
    t.circle(10, 90)

for _ in range(5):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw_bird(x, y)

turtle.done()