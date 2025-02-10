import turtle

x = turtle.Turtle()
x.speed(0)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for i in range(360):
    x.pencolor(colors[i % 6])
    x.width(i // 50 + 1)
    x.forward(i)
    x.left(59)

turtle.done()