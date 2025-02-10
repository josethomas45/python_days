import turtle

def draw_square(x, y, side_length, pen_color, fill_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

def draw_circle(x, y, radius, pen_color, fill_color):
    turtle.penup()
    turtle.goto(x, y - radius)  # Adjust y to start drawing the circle from the bottom
    turtle.pendown()
    turtle.color(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

turtle.shape("turtle")
turtle.color("green")

draw_square(-50, -50, 100, "blue", "yellow")
draw_square(100, 100, 100, "red", "orange")
draw_circle(-100, 100, 50, "purple", "pink")

turtle.done()
