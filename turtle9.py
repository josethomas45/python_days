import turtle
import random

t = turtle.Turtle()

t.shape("turtle")
t.color("green")
color= ["blue", "red", "purple", "orange", "pink"]
t.speed(0)


def make_pentagon(size):
    t.color(color[random.randint(0,4)])
    for _ in range(5):
        t.forward(size)
        t.right(72)
        



def make_rotated_pentagons(size, count, angle):
    for _ in range(count):
        make_pentagon(size)
        t.right(angle-_)
        

make_rotated_pentagons(100, 500, 72)

turtle.done()
